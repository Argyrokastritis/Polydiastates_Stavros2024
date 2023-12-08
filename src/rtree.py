from str_utils import str_diff


class MBR:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax

    def contains(self, x, y, z):
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax and self.zmin <= z <= self.zmax

    def intersects(self, mbr):
        self_contains_mbr_x = self.xmin <= mbr.xmin <= self.xmax or self.xmin <= mbr.xmax <= self.xmax
        mbr_contains_self_x = mbr.xmin <= self.xmin <= mbr.xmax or mbr.xmin <= self.xmax <= mbr.xmax
        intersects_x = self_contains_mbr_x or mbr_contains_self_x
        if intersects_x:
            self_contains_mbr_y = self.ymin <= mbr.ymin <= self.ymax or self.ymin <= mbr.ymax <= self.ymax
            mbr_contains_self_y = mbr.ymin <= self.ymin <= mbr.ymax or mbr.ymin <= self.ymax <= mbr.ymax
            intersects_y = self_contains_mbr_y or mbr_contains_self_y
            if intersects_y:
                self_contains_mbr_z = self.zmin <= mbr.zmin <= self.zmax or self.zmin <= mbr.zmax <= self.zmax
                mbr_contains_self_z = mbr.zmin <= self.zmin <= mbr.zmax or mbr.zmin <= self.zmax <= mbr.zmax
                intersects_z = self_contains_mbr_z or mbr_contains_self_z
                return intersects_z
            else:
                return False
        else:
            return False

    def extend(self, x, y, z):
        new_mbr = MBR(self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax)
        if new_mbr.xmin > x:
            new_mbr.xmin = x
        if new_mbr.xmax < x:
            new_mbr.xmax = x
        if new_mbr.ymin > y:
            new_mbr.ymin = y
        if new_mbr.ymax < y:
            new_mbr.ymax = y
        if new_mbr.zmin > z:
            new_mbr.zmin = z
        if new_mbr.zmax < z:
            new_mbr.zmax = z
        return new_mbr

    def calc_area(self):
        dx = str_diff(self.xmax, self.xmin)
        dy = self.ymax - self.ymin
        dz = self.zmax - self.zmin
        return dx * dy * dz

    def area_increase(self, x, y, z):
        if self.contains(x, y, z):
            return 0
        else:
            extended = self.extend(x, y, z)
            diff = extended.calc_area() - self.calc_area()
            return diff


def find_min_child(children, data):
    min_area = float('inf')
    min_child = children[0]
    for child in children:
        area = child.mbr.area_increase(data.surname, data.awards, data.dblp_records)
        if area < min_area:
            min_area = area
            min_child = child
    return min_child


class RTree:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.mbr = None

        if data is not None:
            self.mbr = MBR(data.surname, data.surname, data.awards, data.awards, data.dblp_records, data.dblp_records)

    def mass_insert(self, arr):
        for item in arr:
            self.insert(item)

    def insert(self, data):
        if len(self.children) < 3:
            self.children.append(RTree(data))
            if self.mbr is None:
                self.mbr = MBR(data.surname, data.surname, data.awards, data.awards, data.dblp_records, data.dblp_records)
            else:
                self.mbr = self.mbr.extend(data.surname, data.awards, data.dblp_records)
        else:
            min_child = find_min_child(self.children, data)
            if not min_child.is_leaf():
                min_child.insert(data)
            else:
                new_node = RTree(min_child.data)
                min_child.data = None
                min_child.children.append(new_node)

    def range_query(self, surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords):
        query_mbr = MBR(surname_min, surname_max, award_min, award_max, min_dblprecords, max_dblprecords)
        if self.is_leaf():
            if surname_min <= self.data.surname <= surname_max and award_min <= self.data.awards <= award_max and min_dblprecords <= self.data.dblp_records <= max_dblprecords:
                return [self.data]
            else:
                return []
        else:
            out = []
            for child in self.children:
                if child is not None and query_mbr.intersects(child.mbr):
                    out.extend(child.range_query(surname_min, surname_max, award_min, award_max,min_dblprecords, max_dblprecords))
            return list(set(out))

    def is_leaf(self):
        return self.data is not None
