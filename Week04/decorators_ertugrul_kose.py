import tracemalloc as tm
from time import time as current_time


def performance(func):
    """
    Decorator that gathers call count, execution time and memory usage.
    """

    performance.count = 0
    performance.time_total = 0.0
    performance.mem_total = 0.0

    def wrapper(*args, **kwargs):
        tm.start()

        start = current_time()
        result = func(*args, **kwargs)
        end = current_time()

        mem_now, mem_peak = tm.get_traced_memory()
        tm.stop()

        performance.count += 1
        performance.time_total += (end - start)
        performance.mem_total += mem_peak

        return result

    return wrapper
