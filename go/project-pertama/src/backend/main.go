package main

import (
	"flag"
	"fmt"
)

func main() {
	var name = flag.String("name", "anonymous", "type your name")
	var age = flag.Int64("age", 25, "type your age")
	var data2 string
	flag.StringVar(&data2, "gender", "male", "type your gender")

	flag.Parse()
	fmt.Printf("name\t: %s\n", *name)
	fmt.Printf("age\t: %d\n", *age)
	fmt.Println(data2)
}
