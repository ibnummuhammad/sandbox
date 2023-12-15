package main

import (
	"fmt"
	"os"
)

func main() {
	var argsRaw = os.Args
	fmt.Println(argsRaw)
	fmt.Printf("-> %#v\n", argsRaw)
	// -> []string{".../bab45", "banana", "potato", "ice cream"}

	var args = argsRaw[1:]
	fmt.Println(args)
	fmt.Printf("-> %#v\n", args)
	// -> []string{"banana", "potatao", "ice cream"}
}
