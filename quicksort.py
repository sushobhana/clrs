

def partition(A, p, r):

    key = A[r]
    i = j = p

    while j < r:
        # print(j)
        if A[j] < key:
            A[j], A[i] = A[i], A[j]
            i += 1
        j += 1

    A[i], A[r] = key, A[i]

    return i


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        # print(q)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def main():
    A = [1, 2, 3, 23, 45, 6, 450, 7, 9, 800]
    quick_sort(A, 0, 9)
    print(A)


if __name__ == '__main__':
    main()