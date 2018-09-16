from core import Sentinel


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


def merge(array, begin, mid, end):

    left_array = []
    for i in range(begin, mid + 1):
        left_array.append(array[i])
    left_array.append(Sentinel())

    right_array = []
    for i in range(mid + 1, end + 1):
        right_array.append(array[i])
    right_array.append(Sentinel())

    # print(left_array, right_array)

    i = j = 0
    for k in range(begin, end + 1):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
    # print(array)


if __name__ == '__main__':
    A = [45, 2, 67, 1, -5, 100, 15]
    merge_sort(A, 0, 6)
    print(A)