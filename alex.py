from helpers import *


@measure_memory
@measure_time()
def extract_list():
    data = list(range(1, 12345))
    step = 3
    while data:
        print(data[:step])
        del data[:step]



if __name__ == '__main__':
    extract_list()
#Total time: 3.230444062999595 seconds.
#Total allocated size in KiB: 230.7
#Total allocated size B: 236218.0
