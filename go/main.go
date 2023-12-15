package main

// fmt package provides the function to print anything
import "fmt"

func main() {

	// define and initialize the string variable using var keyword
	var favSubject string = "Math"

	// printing string with %s specifier
	fmt.Println("What is your favorite subject? (define string using var keyword)")
	fmt.Printf("It's %s\n", favSubject)

	// define string using the shorthand way
	favSports := "Cricket"

	// printing string with %s specifier
	fmt.Println("What is your favorite Sport? (define string by shorthand way)")
	fmt.Printf("It's %s\n", favSports)
}
