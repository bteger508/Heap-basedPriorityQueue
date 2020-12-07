#!/usr/bin/python3
import unittest
import HeapSort

"""
A MaxPriorityQueue module based on CLRS3, chapter 6.5.
Developed by Alex Saunters and Ben Eger.
"""


def insert(x):
    """
    Insert element x into the max priority queue

    :param x: an element to add to the max priority que
    """
    return [10]


def maximum(heap):
    """
    return the element with the largest key

    :return: element with the largest key
    """
    HeapSort.build_max_heap(heap)
    return heap[0]


def extract_max(heap):
    """
    remove and return the element with the largest key

    :return: element with the largest key
    """

    """
        if len(A) < 1:
        raise Exception("heap underflow")
    max = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    HeapSort.max_heapify(A, 0)
    """
    HeapSort.build_max_heap(heap)
    if len(heap) < 1:
        return None
    max = heap.pop(0)
    heap.heap_size -= 1
    HeapSort.max_heapify(heap, 0)
    return max


def increase_key(x, k):
    """
    increase the value of element x's key to the new value k

    :param x: an element in the max priority que
    :param k: the new value for element x
    :type x: element
    :type k: int
    """
    pass


class MaxPriorityQueueTest(unittest.TestCase):
    heap1 = HeapSort.HeapCapable([5, 4, 3])
    heap2 = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
    heap3 = HeapSort.HeapCapable([-5, -10, -14, -15, -20])

    myHeap = HeapSort.HeapCapable([25, 16, 14, 15, 20])
    HeapSort.build_max_heap(myHeap)
    print(myHeap)

    def test_maximum_1(self):
        self.assertEqual(5, maximum(self.heap1))

    def test_maximum_2(self):
        self.assertEqual(27, maximum(self.heap2))

    def test_maximum_3(self):
        self.assertEqual(-5, maximum(self.heap3))

    def test_extract_max_1(self):
        self.assertEqual(5, extract_max(HeapSort.HeapCapable([5, 4, 3])))

    def test_extract_max_2(self):
        actual_heap = HeapSort.HeapCapable([5, 4, 3])
        extract_max(actual_heap)
        expected_heap = HeapSort.HeapCapable([4, 3])
        self.assertEqual(expected_heap, actual_heap)

    def test_extract_max_3(self):
        actual_heap = HeapSort.HeapCapable([5, 4, 3])
        extract_max(actual_heap)
        self.assertEqual(2, actual_heap.heap_size)

    def test_extract_max_4(self):
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        extract_max(actual_heap)
        expected_heap = HeapSort.HeapCapable([25, 20, 14, 15, 16])
        self.assertEqual(expected_heap, actual_heap)

    def test_insert_1(self):
        self.assertEqual([10], insert(10))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
