package main

import (
	"flag"
	"fmt"
)

func main() {
	var pipelineName = flag.String("pipeline_name", "", "pipeline context name")

	flag.Parse()
	fmt.Printf("pipeline_name\t: %s\n", *pipelineName)
}
