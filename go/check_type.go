// Golang program to find the variable type
package main

// importing required packages
import (
	"fmt"
)

// main function
func main() {
	f := true
	st := ""
	a := 1
	d := 1.0
	arr := []string{"Go", "Is", "Fun"}

	fmt.Printf("%T\n", f)
	fmt.Printf("%T\n", st)
	fmt.Printf("%T\n", a)
	fmt.Printf("%T\n", d)
	fmt.Printf("%T\n", arr)
}
