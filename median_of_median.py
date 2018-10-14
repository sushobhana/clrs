from insertion_sort import insertion_sort


def select(A, p, r, n):

    if (r - p + 1) <= 5:
        temp = A[p: r + 1]
        insertion_sort(temp)
        return temp[n-1]

    pivot = pivot_element(A, p, r)
    q = partition(A, p, r, pivot)

    k = q - p + 1

    if n == k:
        return A[q]
    elif n > k:
        return select(A, q + 1, r, n - k)
    else:
        return select(A, p, q - 1, n)


def pivot_element(A, p, r):

    medians = []

    for x in range(p, r, 5):
        upper_limit = x + 4
        if upper_limit > r:
            upper_limit = r
        length = upper_limit - x + 1
        medians.append(select(A, x, upper_limit, length // 2 + 1))

    print(medians)
    return select(medians, 0, len(medians), len(medians) // 2)


def partition(A, p, r, pivot):

    i = j = p

    while j < r:
        # print(j)
        if A[j] == pivot:
            A[j], A[r] = A[r], A[j]
        else:
            if A[j] < pivot:
                A[j], A[i] = A[i], A[j]
                i += 1
            j += 1

    A[i], A[r] = pivot, A[i]
    return i


def main():
    A = [1, 2, 3, 23, 45, 6, 450, 7, 9, 800, 56, 76, 89, 789, 987]
    i = select(A, 0, 14, 15)
    print(i)
    print(A)


if __name__ == '__main__':
    main()

