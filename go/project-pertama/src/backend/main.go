package main

import (
	"flag"
	"fmt"
)

var (
	// inputs
	pipelineName = flag.String("pipeline_name", "", "pipeline context name")
)

func main() {
	flag.Parse()
	fmt.Printf("pipeline_name\t: %s\n", *pipelineName)
}
