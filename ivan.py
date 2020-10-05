from helpers import *


@measure_memory
@measure_time()
def extract_list():
    data = list(range(1, 12345))
    step = 3
    for i in range(0, len(data), step):
         result = data[i:i + step]
         print(result)


if __name__ == '__main__':
    extract_list()

#Total time: 2.9175128579990997 seconds.
#Total allocated size in KiB: 230.8
#Total allocated size B: 236306.0

#lvl2
#Total time: 29.90807560599933 seconds.
#Total allocated size in KiB: 9.1
#Total allocated size B: 9362.0
