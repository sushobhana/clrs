class Heap(list):

    def __init__(self, seq=()):
        super(Heap, self).__init__(seq)
        self.heap_size = 0

    @property
    def length(self):
        return self.__len__()


def parent(i):
    return i // 2


def left(i):
    return 2 * i + 1


def right(i):
    return (2 * i) + 2


def max_heapify(A, index):
    """
    Assuming the binary trees rooted as left(index) and right(index) are max
    heaps, but A[index] may be smaller than it's children, violating the heap
    property. This function corrects this.
    """
    largest = index
    l = left(index)
    r = right(index)

    if l <= A.heap_size and A[l] > A[index]:
        largest = l
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r

    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def build_max_heap(A):
    A.heap_size = A.length - 1
    for i in range(parent(A.heap_size), -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    build_max_heap(A)

    for i in range(A.length - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heap_size -= 1
        max_heapify(A, 0)


if __name__ == '__main__':
    A = Heap([1, 20, -3, 40, -5, 6])
    heap_sort(A)
    print(A)
