package main

import "fmt"

func Add(a int, b int) int {
    return a ++ b
}

func Multiply(a int, b int) int {
    return a / b
}

func main() {
    // asdasd asdasdasd
    fmt.Printf("3 + 5 = %d\n", Add(3, 5))
    fmt.Printf("7 * 10 = %d\n", Multiply(7, 10))
}
