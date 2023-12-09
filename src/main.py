from kd import KDTree
from quad import Quad
from range import Range
from rtree import RTree
from data import generate_data
from lsh import lsh
from experiments import experiments


if __name__ == '__main__':
    length = input("""How many rows of data do you want to generate? (~200 recommended) """)
    data = generate_data(int(length))

    mode = input("""Choose operation mode:\n\t0: k-d tree\n\t1: quad tree\n\t2: range tree\n\t3: r-tree\n""")
    mode = int(mode)

    min_sur = input("""Minimum surname for range query: """)
    max_sur = input("""Maximum surname for range query: """)
    min_aw = input("""Minimum awards for range query: """)
    max_aw = input("""Maximum awards for range query: """)
    min_aw = int(min_aw)
    max_aw = int(max_aw)
    min_dblprecords = input("""Minimum dblp_records for range query: """)
    max_dblprecords = input("""Maximum dblp_records for range query: """)
    min_dblprecords = int(min_dblprecords)
    max_dblprecords = int(max_dblprecords)

    lsh_thresh = input("""Minimum similarity (0-1) for LSH: """)

    range_results = []
    tree = None

    if mode == 0:
        tree = KDTree(data)
    elif mode == 1:
        tree = Quad()
        tree.mass_insert(data)
    elif mode == 2:
        tree = Range(data)
    elif mode == 3:
        tree = RTree()
        tree.mass_insert(data)

    range_results = tree.range_query(min_sur, max_sur, min_aw, max_aw, min_dblprecords, max_dblprecords)
    lsh_results = lsh(range_results, float(lsh_thresh))

    # print results
    print(f'Found {len(lsh_results)} matches:')
    for res in lsh_results:
        print(f"""\tSurname: {res.surname}\n\tAwards: {res.awards}\n\t DBLP_records: {res.dblp_records}\n\t Education: {res.education}\n\t------""")

    # run experiments
    ans = input("""\n\n\nDo you want to run the experiments? (this can take minutes) y/n """)
    if ans == 'y':
        experiments()

    # ask user if they want to exit
    ans = input("""\n\n\nDo you want to exit the multidimensional data structures project?""")
    if ans == 'y':
        exit()
