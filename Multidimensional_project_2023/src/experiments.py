from kd import KDTree
from quad import Quad
from range import Range
from rtree import RTree
from data import generate_data
import time
from statistics import mean


def column(matrix, i):
    return [row[i] for row in matrix]


def experiments():
    scale = 10000
    query_times = []

    print('Running experiments:')
    for i in range(10):
        data = generate_data(1000)
        print(f'Iteration {i+1}/10 running...')
        new_query_row = []

        kd = KDTree(data)
        start = time.time()
        for i in range(scale):
            res1 = kd.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end-start)

        quad = Quad()
        quad.mass_insert(data)
        start = time.time()
        for i in range(scale):
            res2 = quad.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        rangetree = Range(data)
        start = time.time()
        for i in range(scale):
            res3 = rangetree.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        rtree = RTree()
        rtree.mass_insert(data)
        start = time.time()
        for i in range(scale):
            res4 = rtree.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        query_times.append(new_query_row)

    print('Experiment results:')
    print(f'k-d average query time miliseconds: {1000*mean(column(query_times,0))/scale}')
    print(f'quad average query time miliseconds: {1000*mean(column(query_times,1))/scale}')
    print(f'range average query time miliseconds: {1000*mean(column(query_times,2))/scale}')
    print(f'rtree average query time miliseconds: {1000*mean(column(query_times,3))/scale}')


