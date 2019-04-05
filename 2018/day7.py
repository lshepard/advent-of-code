import re
import sys

def time_for_simultaneous_steps(instructions):
    deps = dependencies(instructions)

    # pass in three vars to the recursive method:
    # - current work + end times   {A: 15, B: 30}
    # - current_time (starts at 0, then adds to over time)
    # -
#    return time_to_complete(0, {}, deps, 2, 0)
    return time_to_complete(0, {}, deps, 5, 60)

def time_to_complete(current_time, open_work, remaining_graph, max_workers, extra_seconds):
    print(current_time, open_work)

    if ((len(remaining_graph) == 0) and (len(open_work) == 0)):
        return current_time

    # ok, first check if there are any open workers; if so then add the step
    # and recurse
    if len(open_work) < max_workers:
        # add one to the queue
        next_step = next((step for (step, dependencies) in sorted(remaining_graph.items()) if len(dependencies) == 0 and step not in open_work),
                         None)

        # if either the graph is empty, or there are no unblocked elements right now, then skip ahead
        if next_step is not None:
            duration = ord(next_step) - 64 + extra_seconds # ord('A') is 65, but it is supposed to be 1, so subtract
            open_work[next_step] = current_time + duration

            return time_to_complete(current_time,
                                    open_work,
                                    remaining_graph, # we don't remove it until it's done
                                    max_workers,
                                    extra_seconds)

    
    # next check if any workers are coming off, if so complete their work and
    # recurse
    next_step = min(open_work, key=open_work.get)
    new_time = open_work.pop(next_step)

    # moves ahead to the next time that work is completed
    return time_to_complete(new_time,
                            open_work, # now with element popped
                            dependency_graph_minus_step(remaining_graph, next_step),
                            max_workers,
                            extra_seconds)

def correct_order(instructions):
    """Takes a list of instructions, finds out the order they should be operated on"""
    # build dependency graph
    deps = dependencies(instructions)

    # then iterate on it
    return next_step("",deps)

def next_step(current_path, remaining_graph):
    """Recursive function to figure out the path"""
    if len(remaining_graph) == 0:
        return current_path

    nextstep = next(step for (step, dependencies) in sorted(remaining_graph.items()) if len(dependencies) == 0)
    return next_step(current_path + nextstep, dependency_graph_minus_step(remaining_graph, nextstep))
                     
def dependency_graph_minus_step(remaining_graph, nextstep):
    return dict((step, [d for d in deps if d != nextstep]) for (step,deps) in remaining_graph.items() if step != nextstep)
    
def dependencies(instructions):
    """Returns a dict that represents the dependencies"""
    r = re.compile("Step (.*) must be finished before step (.*) can begin.")
    dependents = {}
    for step, dependent in [r.match(instruction).groups() for instruction in instructions]:
        if dependent not in dependents:
            dependents[dependent] = []
        if step not in dependents:
            dependents[step] = []
        
        dependents[dependent] += step

    return dependents # ensures lexical ordering of hash keys
        

if __name__ == "__main__":
    instructions = sys.stdin.readlines()
    print(correct_order(instructions))
    print(time_for_simultaneous_steps(instructions))
