from core import Sentinel


def counting_inversion(array, p, r):
    if p < r:
        q = (p + r) // 2
        count = 0
        count += counting_inversion(array, p, q)
        count += counting_inversion(array, q + 1, r)
        count += counting(array, p, q, r)
        return count
    else:
        return 0


def counting(array, begin, mid, end):

    left_array = []
    for i in range(begin, mid + 1):
        left_array.append(array[i])
    left_array.append(Sentinel())

    right_array = []
    for i in range(mid + 1, end + 1):
        right_array.append(array[i])
    right_array.append(Sentinel())

    # print(left_array, right_array)

    count = 0
    length = mid - begin + 1
    i = j = 0

    for k in range(begin, end + 1):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            # print(left_array,right_array, length, i, length-i)
            if not isinstance(left_array[i], Sentinel):
                count += length - i
            # print(i, j)
                for l in range(i, len(left_array) - 1):
                    print(left_array[l], right_array[j])
            array[k] = right_array[j]
            j += 1

    # print(left_array, right_array, count)

    return count


if __name__ == '__main__':
    A = [2, 3, 8, 6, 1]
    a = counting_inversion(A, 0, 4)
    # print(a)