# Test script to read from FSx with parallelism

import multiprocessing as mp

import os

def read_file(file_name):
    file_name = '/opt/ml/input/data/fsx/' + file_name

    f = open(file_name)
    the_lines = f.readlines()
    f.close

def parallel_read():
    data = os.listdir('/opt/ml/input/data/fsx')
    print(data[0])
    print(len(data))


    pool = mp.Pool(mp.cpu_count())

    results = pool.map(read_file, [x for x in data])

    pool.close()

if __name__ == '__main__':
    print("Starting .......")
    parallel_read()
    print("Finished .......")
