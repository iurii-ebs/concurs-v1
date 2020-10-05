from helpers import *


@measure_memory
@measure_time()
def extract_list():
    data = list(range(1, 12345))
    step = 3
    while data:
        chunk, data = data[:step], data[step:]
        print(chunk)


if __name__ == '__main__':
    extract_list()
#Total time: 11.492088078000961 seconds.
#Total allocated size in KiB: 230.8
#Total allocated size B: 236354.0
