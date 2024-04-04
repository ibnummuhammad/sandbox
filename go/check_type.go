package main

import (
	"fmt"
	"reflect"
)

func main() {
	t1 := "text"
	t2 := []string{"apple", "strawberry", "blueberry"}
	t3 := map[string]float64{"strawberry": 3.2, "blueberry": 1.2}
	t4 := 2
	t5 := 4.5
	t6 := true

	fmt.Printf("t1: %s\n", reflect.TypeOf(t1))
	fmt.Printf("t2: %s\n", reflect.TypeOf(t2))
	fmt.Printf("t3: %s\n", reflect.TypeOf(t3))
	fmt.Printf("t4: %s\n", reflect.TypeOf(t4))
	fmt.Printf("t5: %s\n", reflect.TypeOf(t5))
	fmt.Printf("t6: %s\n", reflect.TypeOf(t6))
}
