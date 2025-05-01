package main

import (
	"fmt"
	"service-order/kubus"
)

func main() {
	fmt.Println("this is main")
	angka := kubus.Kubus{3}
	kotak := angka.Keliling()
	fmt.Printf("%f\n", kotak)
}
