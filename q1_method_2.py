# method 2
def find_smallest_difference(a, b):
    if not a or not b:
        raise Exception("invalid list")
    a.sort()
    b.sort()
    i = j = 0
    diff = abs(a[i] - b[j])
    element_a = a[i]
    element_b = b[j]
    while i < len(a) and j < len(b):
        curr_diff = abs(a[i] - b[j])
        if curr_diff < diff:
            # assume if there are multiple smallest difference return the first pair
            diff = curr_diff
            element_a = a[i]
            element_b = b[j]
        if a[i] >= b[j]:
            j += 1
        else:
            i += 1
    return element_a, element_b, diff


def test_1():
    a = [10, 15, 2, 4]
    b = [0, 18, 6, 11]
    element_a, element_b, diff = find_smallest_difference(a, b)
    assert element_a == 10
    assert element_b == 11
    assert diff == 1


def test_2():
    a = [0]
    b = [0]
    element_a, element_b, diff = find_smallest_difference(a, b)
    assert element_a == 0
    assert element_b == 0
    assert diff == 0


def test_3():
    a = [0, 1, 4]
    b = [-10, -5]
    element_a, element_b, diff = find_smallest_difference(a, b)
    assert element_a == 0
    assert element_b == -5
    assert diff == 5

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()

























