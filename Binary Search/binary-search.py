def binarySearch(arr, target):
    L, r = 0, len(arr) - 1

    while L <= r:
        m = (L + r) // 2

        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            L = m + 1

    return


if __name__ == '__main__':
    assert (binarySearch([1, 3, 5, 6, 7], 3) == 1)
