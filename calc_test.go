package main

import (
  "testing"
)

func TestAdd(t *testing.T) {
    if Add(3, 5) != 8 {
        t.Errorf("Add(3, 5) got %d, want 8", Add(3, 5))
    }
}

func TestMul(t *testing.T) {
    if Multiply(4, 5) != 20 {
	t.Errorf("Multiply(4, 5) got %d, want 20", Multiply(4, 5))
    }
}
