package main

import (
	"flag"
	"fmt"
)

var (
	// inputs
	pipelineName      = flag.String("pipeline_name", "", "pipeline context name")
	runID             = flag.String("run_id", "", "pipeline run uid")
	componentSpecJson = flag.String("component", "{}", "component spec")
	taskSpecJson      = flag.String("task", "", "task spec")
	runtimeConfigJson = flag.String("runtime_config", "", "jobruntime config")
	iterationIndex    = flag.Int("iteration_index", -1, "iteration index, -1 means not an interation")
)

func main() {
	flag.Parse()
	fmt.Printf("pipeline_name\t: %s\n", *pipelineName)
	fmt.Printf("run_id\t: %s\n", *runID)
	fmt.Printf("component\t: %s\n", *componentSpecJson)
	fmt.Printf("task\t: %s\n", *taskSpecJson)
	fmt.Printf("runtime_config\t: %s\n", *runtimeConfigJson)
	fmt.Printf("iteration_index\t: %d\n", *iterationIndex)
}
