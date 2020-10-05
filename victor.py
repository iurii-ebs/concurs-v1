from helpers import *

@measure_memory
@measure_time()
def extract_list():
    data = list(range(1, 12345))
    step = 3
    for i in range(0, len(data), step):
        print(data[i:i+step])


if __name__ == '__main__':
    extract_list()
#Total time: 2.9073842780017003 seconds.
#Total allocated size in KiB: 9.1
#Total allocated size B: 9298.0

#lvl2
#Total time: 30.245711072999256 seconds.
#Total allocated size in KiB: 230.7
#Total allocated size B: 236242.0


