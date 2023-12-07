class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.twod_subtree = None


class Range:
    def __init__(self, data, dimension=0):
        self.root = None
        self.dimension = dimension
        self.build_tree(data)

    def build_tree(self, data):
        if not data:
            return

        if self.dimension == 1:
            data = sorted(data, key=lambda x: x.awards)
        else:
            data = sorted(data, key=lambda x: x.surname)

        mid = len(data) // 2
        self.root = Node(data[mid])
        if data[:mid]:
            self.root.left = Range(data[:mid], self.dimension)
        if data[mid + 1:]:
            self.root.right = Range(data[mid + 1:], self.dimension)
        if self.dimension == 0:
            self.root.twod_subtree = Range(data, 1)

    def query_nodes(self, low, high, deep=False):
        out = []
        comparison = self.root.data.surname
        if self.dimension == 1:
            comparison = self.root.data.awards

        if low <= comparison <= high:
            out.append(self.root)
            if deep:
                if low < comparison and self.root.left is not None:
                    out.extend(self.root.left.query_nodes(low, high, deep))
                if high > comparison and self.root.right is not None:
                    out.extend(self.root.right.query_nodes(low, high, deep))
        else:
            if low < comparison and self.root.left is not None:
                out.extend(self.root.left.query_nodes(low, high, deep))
            if high > comparison and self.root.right is not None:
                out.extend(self.root.right.query_nodes(low, high, deep))

        return out

    def range_query(self, surname_min, surname_max, award_min, award_max):
        out = []
        results = self.query_nodes(surname_min, surname_max)
        for r in results:
            results2 = r.twod_subtree.query_nodes(award_min, award_max, deep=True)
            for r2 in results2:
                data = r2.data
                if surname_min <= data.surname <= surname_max and award_min <= data.awards <= award_max:
                    out.append(data)

        return out
