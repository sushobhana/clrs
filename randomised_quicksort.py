import random

from quicksort import partition, quick_sort


def randomised_partition(A, p, r):
    random_index = random.randint(p, r)
    A[r], A[random_index] = A[random_index], A[r]
    return partition(A, p, r)


def randomised_quick_sort(A, p, r):
    if p < r:
        q = randomised_partition(A, p, r)
        # print(q)
        randomised_quick_sort(A, p, q - 1)
        randomised_quick_sort(A, q + 1, r)


def main():
    A = [1, 2, 3, 23, 45, 6, 450, 7, 9, 800]
    quick_sort(A, 0, 9)
    print(A)


if __name__ == '__main__':
    main()
