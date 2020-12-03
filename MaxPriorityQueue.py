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


def maximum(array):
    """
    return the element with the largest key

    :return: element with the largest key
    """
    return array[0]


def extract_max(A):
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
    if len(A) < 1:
        return None
    return A.pop(0)

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
    def test_maximum_1(self):
        self.assertEqual(maximum([5, 4, 3]), 5)

    def test_maximum_2(self):
        self.assertEqual(maximum([27, 16, 25, 14, 15, 20]), 27)

    def test_maximum_3(self):
        self.assertEqual(maximum([-5, -10, -14, -15, -20]), -5)

    def test_extract_max_1(self):
        self.assertEqual(extract_max(HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])), 27)

    def test_extract_max_2(self):
        test_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        extract_max(test_heap)
        self.assertEqual([16, 25, 14, 15, 20], test_heap)

    def test_extract_max_3(self):
        test_heap = HeapSort.HeapCapable([])
        self.assertIsNone(extract_max(test_heap))

    def test_insert_1(self):
        self.assertEqual(insert(10), [10])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
