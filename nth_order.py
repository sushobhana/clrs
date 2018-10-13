from randomised_quicksort import randomised_partition


def select(A, p, r, n):

    q = randomised_partition(A, p, r)

    k = q - p + 1

    if n == k:
        return A[q]
    elif n > k:
        return select(A, q + 1, r, n - k)
    else:
        return select(A, p, q - 1, n)


def main():
    A = [1, 2, 3, 23, 45, 6, 450, 7, 9, 800]
    i = select(A, 0, 9, 8)
    print(i)


if __name__ == '__main__':
    main()
