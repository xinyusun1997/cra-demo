// The main package.
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand/v2"
	"strconv"
	"time"

	"cloud.google.com/go/pubsub"
)

func main() {
	ctx := context.Background()
	if err := run(ctx); err != nil {
		log.Fatalf("Failed to run: %v", err)
	}
}

// run publishes to an existing pubsub topic and subscription.
func run(ctx context.Context) error {
	client, err := pubsub.NewClient(ctx, "umairidris-anthos-dev")
	if err != nil {
		return fmt.Errorf("failed to create client: %v", err)
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	donec := make(chan struct{})
	exitc := make(chan struct{})

	// Run workers.
	numWorkers := 2

	for i := 0; i < numWorkers; i++ {
		go func() {
			sub := client.Subscription("test-sub")
			f := func(ctx context.Context, msg *pubsub.Message) {
				log.Printf("Worker %d Received message: %v", i, string(msg.Data))
				time.Sleep(10 * time.Second)
				msg.Ack()
				donec <- struct{}{}
			}
			if err := sub.Receive(ctx, f); err != nil {
				log.Printf("Worker %d failed to receive: %v", i, err)
			}
			exitc <- struct{}{}
		}()
	}

	// Publish messages.
	topic := client.Topic("test-topic")
	id := strconv.Itoa(rand.IntN(1000))
	topic.EnableMessageOrdering = true

	// Append a random number to the messages to differentiate them from leftover messages from
	// previous runs.
	msgs := []*pubsub.Message{
		{Data: []byte("message1 " + id), OrderingKey: "key1"},
		{Data: []byte("message2 " + id), OrderingKey: "key1"},
		{Data: []byte("message3 " + id), OrderingKey: "key2"},
	}
	for _, msg := range msgs {
		if _, err := topic.Publish(ctx, msg).Get(ctx); err != nil {
			return fmt.Errorf("failed to publish: %v", err)
		}
	}
	log.Printf("Published messages")

	// Wait for workers to finish.
	for i := 0; i < len(msgs); i++ {
		<-donec
	}

	// Cancel context to stop workers.
	cancel()

	// Wait for workers to exit.
	for i := 0; i < numWorkers; i++ {
		<-exitc
	}
	return nil
}
