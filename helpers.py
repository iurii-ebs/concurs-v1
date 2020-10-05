import time
import timeit
import tracemalloc

from functools import wraps



def measure_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        total = sum(stat.size for stat in top_stats)

        tracemalloc.stop()
        print("Total allocated size in KiB: %.1f" % (total / 1024))
        print("Total allocated size B: %.1f" % total)

    return wrapper


def measure_time(iterations=999):
    def measure(func):

        def wrapper(*args, **kwargs):
            total = timeit.timeit(func, number=iterations)
            print(f'Total time: {total} seconds.')

        return wrapper

    return measure
