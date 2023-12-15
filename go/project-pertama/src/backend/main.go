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

	// container inputs
	dagExecutionID    = flag.Int64("dag_execution_id", 0, "DAG execution ID")
	containerSpecJson = flag.String("container", "{}", "container spec")
	k8sExecConfigJson = flag.String("kubernetes_config", "{}", "kubernetes executor config")

	// config
	mlmdServerAddress = flag.String("mlmd_server_address", "", "MLMD server address")
	mlmdServerPort    = flag.String("mlmd_server_port", "", "MLMD server port")

	// output paths
	executionIDPath    = flag.String("execution_id_path", "", "Exeucution ID output path")
	iterationCountPath = flag.String("iteration_count_path", "", "Iteration Count output path")
	podSpecPatchPath   = flag.String("pod_spec_patch_path", "", "Pod Spec Patch output path")
	// the value stored in the paths will be either 'true' or 'false'
	cachedDecisionPath = flag.String("cached_decision_path", "", "Cached Decision output path")
	conditionPath      = flag.String("condition_path", "", "Condition output path")
)

func main() {
	flag.Parse()
	fmt.Printf("pipeline_name\t: %s\n", *pipelineName)
	fmt.Printf("run_id\t: %s\n", *runID)
	fmt.Printf("component\t: %s\n", *componentSpecJson)
	fmt.Printf("task\t: %s\n", *taskSpecJson)
	fmt.Printf("runtime_config\t: %s\n", *runtimeConfigJson)
	fmt.Printf("iteration_index\t: %d\n", *iterationIndex)
	fmt.Printf("dag_execution_id\t: %d\n", *dagExecutionID)
	fmt.Printf("container\t: %s\n", *containerSpecJson)
	fmt.Printf("kubernetes_config\t: %s\n", *k8sExecConfigJson)
	fmt.Printf("mlmd_server_address\t: %s\n", *mlmdServerAddress)
	fmt.Printf("mlmd_server_port\t: %s\n", *mlmdServerPort)
	fmt.Printf("execution_id_path\t: %s\n", *executionIDPath)
	fmt.Printf("iteration_count_path\t: %s\n", *iterationCountPath)
	fmt.Printf("pod_spec_patch_path\t: %s\n", *podSpecPatchPath)
	fmt.Printf("cached_decision_path\t: %s\n", *cachedDecisionPath)
	fmt.Printf("condition_path\t: %s\n", *conditionPath)
}
