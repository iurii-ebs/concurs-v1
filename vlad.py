from helpers import *


@measure_memory
@measure_time()
def extract_list():
    data = list(range(1, 12345))
    step = 3
    length = int(len(data) / step)
    [print([data[item * step], data[item * step + 1], data[item * step + 2]]) for item in range(length)]
    print([data[length * step + item] for item in range(len(data) % step)])



if __name__ == '__main__':
    extract_list()

#Total time: 3.027717203996872 seconds.
#Total allocated size in KiB: 231.7
#Total allocated size B: 237226.0

