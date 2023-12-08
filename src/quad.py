from str_utils import str_average


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Node(object):
    def __init__(self, pos, data):
        self.pos = pos
        self.data = data


class Quad(object):
    def __init__(self, top_left=Point('', 0 ,0), bot_right=Point('zzzzzzzzzz', 30 ,200),n=None, top_left_tree=None, top_right_tree=None,
                 bot_left_tree=None, bot_right_tree=None, min_dblprecords=0, max_dblprecords=0):
        self.top_left = top_left
        self.bot_right = bot_right
        self.n = n
        self.top_left_tree = top_left_tree
        self.top_right_tree = top_right_tree
        self.bot_left_tree = bot_left_tree
        self.bot_right_tree = bot_right_tree
        self.min_dblprecords = min_dblprecords
        self.max_dblprecords = max_dblprecords

    def insert(self, node):
        if node is None:
            return

        # only change node data if it is a leaf node, and doesnt already have data
        if self.n is None and self.is_leaf():
            self.n = node
            return
        # if not leaf node OR data exists, we need to divide deeper
        else:
            old_node = self.n  # save old data to re-insert later
            self.n = None  # delete node data (only leaf nodes have data)

            # divide tree into 8 subtrees
            if str_average(self.top_left.x, self.bot_right.x) >= node.pos.x:
                if (self.top_left.y + self.bot_right.y) / 2 >= node.pos.y:
                    if (self.top_left.z + self.bot_right.z) / 2 >= node.pos.z:
                        # print('top left')
                        if self.top_left_tree is None:
                            self.top_left_tree = Quad(
                                Point(self.top_left.x, self.top_left.y, self.top_left.z),
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.top_left_tree.insert(node)
                    else:
                        if self.bot_left_tree is None:
                            self.bot_left_tree = Quad(
                                Point(self.top_left.x, self.top_left.y, (self.top_left.z + self.bot_right.z) / 2),
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      self.bot_right.z),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.bot_left_tree.insert(node)
                else:
                    if (self.top_left.z + self.bot_right.z) / 2 >= node.pos.z:
                        if self.top_right_tree is None:
                            self.top_right_tree = Quad(
                                Point(str_average(self.top_left.x, self.bot_right.x), self.top_left.y, self.top_left.z),
                                Point(self.bot_right.x,
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.top_right_tree.insert(node)
                    else:
                        if self.bot_right_tree is None:
                            self.bot_right_tree = Quad(
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                Point(self.bot_right.x, self.bot_right.y, self.bot_right.z),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                            self.bot_right_tree.insert(node)
            else:
                if (self.top_left.y + self.bot_right.y) / 2 >= node.pos.y:
                    if (self.top_left.z + self.bot_right.z) / 2 >= node.pos.z:
                        if self.top_left_tree is None:
                            self.top_left_tree = Quad(
                                Point(self.top_left.x, self.top_left.y, self.top_left.z),
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.top_left_tree.insert(node)
                    else:
                        if self.bot_left_tree is None:
                            self.bot_left_tree = Quad(
                                Point(self.top_left.x, self.top_left.y, (self.top_left.z + self.bot_right.z) / 2),
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      self.bot_right.z),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.bot_left_tree.insert(node)
                else:
                    if (self.top_left.z + self.bot_right.z) / 2 >= node.pos.z:
                        if self.top_right_tree is None:
                            self.top_right_tree = Quad(
                                Point(str_average(self.top_left.x, self.bot_right.x), self.top_left.y, self.top_left.z),
                                Point(self.bot_right.x,
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                        self.top_right_tree.insert(node)
                    else:
                        if self.bot_right_tree is None:
                            self.bot_right_tree = Quad(
                                Point(str_average(self.top_left.x, self.bot_right.x),
                                      (self.top_left.y + self.bot_right.y) / 2,
                                      (self.top_left.z + self.bot_right.z) / 2),
                                Point(self.bot_right.x, self.bot_right.y, self.bot_right.z),
                                min_dblprecords=self.min_dblprecords, max_dblprecords=self.max_dblprecords)
                            self.bot_right_tree.insert(node)

            # re-insert old data if needed
            if old_node is not None:
                self.insert(old_node)

    def mass_insert(self, data_array):
        for d in data_array:
            new_point = Point(d.surname, d.awards, d.dblp_records)
            new_node = Node(new_point, d)
            self.insert(new_node)

    def print(self, i=0):
        if self.n is not None:
            print(self.n.data.surname)

        if self.top_left_tree is not None:
            print(f'top left {i}')
            self.top_left_tree.print(i + 1)
        if self.top_right_tree is not None:
            print(f'top right {i}')
            self.top_right_tree.print(i + 1)
        if self.bot_left_tree is not None:
            print(f'bot left {i}')
            self.bot_left_tree.print(i + 1)
        if self.bot_right_tree is not None:
            print(f'bot right {i}')
            self.bot_right_tree.print(i + 1)

    def is_leaf(self):
        return self.top_left_tree is None and self.top_right_tree is None \
            and self.bot_left_tree is None and self.bot_right_tree is None

    def intersect(self, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords):
        return not (
                surname_min > self.bot_right.x
                or surname_max < self.top_left.x
                or award_min > self.bot_right.y
                or award_max < self.top_left.y
                or min_dblprecords > self.bot_right.z
                or max_dblprecords < self.top_left.z
        )

    def range_query(self, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords):
        out = []

        if not self.intersect(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords):
            return out

        if self.is_leaf():
            data = self.n.data
            if surname_min <= data.surname <= surname_max and award_min <= data.awards <= award_max and min_dblprecords <= data.dblp_records <= max_dblprecords:
                out.append(data)
                return out

        if self.top_left_tree is not None:
            out += self.top_left_tree.range_query(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)
        if self.top_right_tree is not None:
            out += self.top_right_tree.range_query(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)
        if self.bot_left_tree is not None:
            out += self.bot_left_tree.range_query(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)
        if self.bot_right_tree is not None:
            out += self.bot_right_tree.range_query(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)

        return out

    def in_boundary(self, p):
        return self.top_left.x <= p.x <= self.bot_right.x and self.top_left.y <= p.y <= self.bot_right.y
