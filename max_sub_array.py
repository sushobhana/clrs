def find_max_crossing_subarray(A, low, mid, high):

    left_sum = A[mid]
    left_index = mid
    sum = A[mid]
    for i in range(mid - 1, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i

    right_sum = A[mid + 1]
    right_index = mid + 1
    sum = A[mid + 1]
    for i in range(mid + 2, high + 1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            right_index = i
    # print (low, mid, high, left_sum , right_sum)
    return left_index, right_index, left_sum + right_sum


def max_subarray(A, low, high):

    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_right, left_max = max_subarray(A, low, mid)
        right_low, right_right, right_max = max_subarray(A, mid+1, high)
        cross_low, cross_right, cross_max = find_max_crossing_subarray(A, low, mid, high)

        if left_max > cross_max and left_max > right_max:
            return left_low, left_right, left_max
        elif right_max > cross_max:
            return right_low, right_right, right_max
        else:
            return cross_low, cross_right, cross_max


if __name__ == '__main__':
    A = [1, -4, 3, 4, -2, 6]
    l, r, sum = max_subarray(A, 0, 5)
    print(l, r, sum)


