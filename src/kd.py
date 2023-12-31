class KDTree(object):
    def __init__(self, points):
        # It recursively constructs a 2D tree from the points list and returns the root node of the tree
        def make(points, i=0):
            if len(points) > 1:
                key = lambda x: x.surname
                if i == 1:
                    key = lambda x: x.awards
                if i == 2:
                    key = lambda x: x.dblp_records
                points = sorted(points, key=key)
                i = (i + 1) % 3

                m = len(points) >> 1
                return [make(points[:m], i), make(points[m + 1:], i),
                        points[m]]
            if len(points) == 1:
                return [None, None, points[0]]

        def range_query(node, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords, i=0):
            out = []

            if surname_max >= node[2].surname >= surname_min and award_max >= node[2].awards >= award_min and max_dblprecords >= node[2].dblp_records >= min_dblprecords:
                out.append(node[2])

            if i == 0:
                if node[2].surname >= surname_min and node[0] is not None:
                    out = out + range_query(node[0], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,1)
                if node[2].surname <= surname_max and node[1] is not None:
                    out = out + range_query(node[1], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,1)
            elif i == 1:
                if node[2].awards >= award_min and node[0] is not None:
                    out = out + range_query(node[0], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,2)
                if node[2].awards <= award_max and node[1] is not None:
                    out = out + range_query(node[1], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,2)
            elif i == 2:
                if node[2].dblp_records >= min_dblprecords and node[0] is not None:
                    out = out + range_query(node[0], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,0)
                if node[2].dblp_records <= max_dblprecords and node[1] is not None:
                    out = out + range_query(node[1], surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords,0)

            return out

        self._range_query = range_query
        self._root = make(points)

    def range_query(self, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords):
        return self._range_query(self._root, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)
