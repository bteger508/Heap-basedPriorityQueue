#!/usr/bin/python3
import math
import unittest
import HeapSort

"""
A MaxPriorityQueue module based on CLRS3, chapter 6.5.
Developed by Alex Saunters and Ben Eger.
"""


def insert(heap, key):
    """
    Insert element x into the max priority queue

    :param heap: ...
    :param key: ...
    """
    heap.heap_size += 1
    heap.append(-math.inf)
    increase_key(heap, heap.heap_size-1, key)


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


def increase_key(heap, i, key):
    """
    increase the value of element x's key to the new value k

    :param heap: ...
    :param i: index of the element in the max priority que
    :param key: the new value for element x
    :type i: index
    :type key: int
    """
    if key < heap[i]:
        return "new key is smaller than current key"
    heap[i] = key
    while i > 0 and heap[HeapSort.parent(i)] < heap[i]:
        heap[i], heap[HeapSort.parent(i)] = heap[HeapSort.parent(i)], heap[i]
        i = HeapSort.parent(i)


class MaxPriorityQueueTest(unittest.TestCase):
    heap1 = HeapSort.HeapCapable([5, 4, 3])
    heap2 = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
    heap3 = HeapSort.HeapCapable([-5, -10, -14, -15, -20])

    myHeap = HeapSort.HeapCapable([9001, 27, 16, 25, 14, 15, 20])
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

    def test_increase_key_1(self):
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        increase_key(actual_heap, 3, 35)
        expected_heap = HeapSort.HeapCapable([35, 27, 25, 16, 15, 20])
        self.assertEqual(expected_heap, actual_heap)

    def test_increase_key_2(self):
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        increase_key(actual_heap, 0, 9001)
        expected_heap = HeapSort.HeapCapable([9001, 16, 25, 14, 15, 20])
        self.assertEqual(expected_heap, actual_heap)

    def test_insert_1(self):
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        insert(actual_heap, 90001)
        expected_heap = HeapSort.HeapCapable([9001, 27, 20, 25, 14, 15, 16])    # This expected heap is likely incorrect
        self.assertEqual(expected_heap, actual_heap)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
