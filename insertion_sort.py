def insertion_sort(A):
    """Applying insertion sort on array A"""

    for j, key in enumerate(A):
        # Insert key to the sorted sequence A[0...j-1]

        # i indicates the index of the element in the sorted range which is
        # going to be replaced by key.
        i = j-1

        while (i >= 0) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key


if __name__ == '__main__':
    A = [45, 2, 67, 1, -5, 100, 15]
    insertion_sort(A)
    print(A)