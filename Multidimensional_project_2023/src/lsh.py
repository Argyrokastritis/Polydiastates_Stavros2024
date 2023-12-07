def lsh(data, threshold):
    out = []
    for d1 in data:
        temp = d1
        if not out:
            out.append(d1)
            continue
        for d2 in out:
            if lsh_ratio(d1.education, d2.education) < threshold:
                temp = None
                break
        if temp is not None:
            out.append(temp)
    return out


def lsh_ratio(vector1, vector2):
    max_length = max(len(vector1), len(vector2))
    return count_equal_elements(vector1, vector2) / max_length


def count_equal_elements(vector1, vector2):
    count = 0
    for e in vector1:
        if e in vector2:
            count += 1
    return count

