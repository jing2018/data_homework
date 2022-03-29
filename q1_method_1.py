# method 1
def find_smallest_difference_v1(a, b):
    diff = abs(a[0] - b[0])
    element_a = a[0]
    element_b = b[0]
    for i in a:
        for j in b:
            curr_diff = abs(i-j)
            if curr_diff < diff:
                # assume if there are multiple smallest difference return the first pair
                diff = curr_diff
                element_a = i
                element_b = j
    return element_a, element_b, diff


def test_1():
    a = [10, 15, 2, 4]
    b = [0, 18, 6, 11]
    element_a, element_b, diff = find_smallest_difference_v1(a, b)
    assert element_a == 10
    assert element_b == 11
    assert diff == 1


def test_2():
    a = [0]
    b = [0]
    element_a, element_b, diff = find_smallest_difference_v1(a, b)
    assert element_a == 0
    assert element_b == 0
    assert diff == 0


def test_3():
    a = [0, 1, 4]
    b = [-10, -5]
    element_a, element_b, diff = find_smallest_difference_v1(a, b)
    assert element_a == 0
    assert element_b == -5
    assert diff == 5

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
