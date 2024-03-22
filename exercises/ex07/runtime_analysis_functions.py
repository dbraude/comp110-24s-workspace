import numpy as np
import timeit
import tracemalloc

MAX_VAL: int = 10 ** 5

def random_descending_list(n: int) -> list[int]:
    """Generate a list of random descending integers."""
    new_list: list[int] = []
    return new_list

def evaluate_runtime(fn_name, start_size: int, end_size: int) -> np.array:
    """Evaluate the runtime for different size inputs."""
    from exercises.ex07.sort_functions import selection_sort, insertion_sort
    NUM_TRIALS: int = 1
    times: list[float] = []
    for inp_size in range(start_size, end_size+1):
        l: list[int] = random_descending_list(inp_size)
        call_command: str = f"{fn_name}(l)"
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        result = timeit.timeit(stmt=call_command, globals=locals(), number=NUM_TRIALS)
        times.append(result/NUM_TRIALS)
    print(f"Runtime of {fn_name} for input of size {end_size}: {round(result/NUM_TRIALS, 2)} seconds")
    return np.array(times)

def evaluate_memory_usage(fn_name, start_size: int, end_size: int):
    from exercises.ex07.sort_functions import selection_sort, insertion_sort
    usage: list[float] = []
    for inp_size in range(start_size, end_size+1):
        l: list[int] = random_descending_list(inp_size)
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        tracemalloc.start()
        locals()[fn_name](l)
        result = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        usage.append(result[1])
    print(f"Memory usage of {fn_name} for input of size {end_size}: {result[1]} blocks of memory.")
    return np.array(usage)