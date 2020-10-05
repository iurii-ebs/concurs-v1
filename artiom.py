from helpers import *
from itertools import islice


@measure_memory
@measure_time()
def extract_list():
    arr = list(range(1, 12345))
    size = 3
    limit = (len(arr) // size) * size
    pages = islice(arr, 0, limit)
    for page in zip(*[pages]*size):
        print(page)
    remain = arr[limit:]
    if remain:
        print(tuple(remain))

if __name__ == '__main__':
    extract_list()

#Total time: 2.677901371000189 seconds.
#Total allocated size in KiB: 230.8
#Total allocated size B: 236322.0

#lvl2
#Total time: 27.320294098000886 seconds.
#Total allocated size in KiB: 230.8
#Total allocated size B: 236322.0
