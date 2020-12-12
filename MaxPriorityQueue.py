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
    Insert key into the max priority queue.

            .. note:: This function modifies the heap in place and will not return anything.

    :param heap: the heap to be modified
    :param key: the key to be inserted into the max priority queue
    :type heap: heapsort_skeleton.HeapCapable
    :type key: int
    """

    heap.heap_size += 1
    heap.append(-math.inf)
    increase_key(heap, heap.heap_size-1, key)


def maximum(heap):
    """
    Return the element with the largest key.

    :param heap: the heap to be accessed
    :type heap: heapsort_skeleton.HeapCapable
    :return: the element with the largest key
    :rtype: int
    """

    HeapSort.build_max_heap(heap)
    return heap[0]


def extract_max(heap):
    """
    Remove and return the element with the largest key.

    :param heap: the heap to be modified
    :type heap: heapsort_skeleton.HeapCapable
    :return: the element with the largest key
    :rtype: int
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
    Increase the value of element x's key to the new value k.

        .. note:: This function modifies the heap in place, and will only return an error message if the new key is smaller than the existing key.

    :param heap: the heap to be modified
    :param i: index of the element in the max priority que
    :param key: the new value for element x
    :type heap: heapsort_skeleton.HeapCapable
    :type i: index
    :type key: int
    :return: an error message that returns only if the new key is smaller than the existing key
    :rtype: string
    """

    if key < heap[i]:
        return "new key is smaller than existing key"
    heap[i] = key
    while i > 0 and heap[HeapSort.parent(i)] < heap[i]:
        heap[i], heap[HeapSort.parent(i)] = heap[HeapSort.parent(i)], heap[i]
        i = HeapSort.parent(i)


class MaxPriorityQueueTest(unittest.TestCase):
    heap1 = HeapSort.HeapCapable([5, 4, 3])
    heap2 = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
    heap3 = HeapSort.HeapCapable([-5, -10, -14, -15, -20])

    def test_maximum_1(self):
        self.assertEqual(5, maximum(self.heap1))

    def test_maximum_2(self):
        self.assertEqual(27, maximum(self.heap2))

    def test_maximum_3(self):
        self.assertEqual(-5, maximum(self.heap3))

    def test_extract_max_small_heap(self):
        """
        extract_max: general case with a 3 element array
        """
        self.assertEqual(5, extract_max(HeapSort.HeapCapable([5, 4, 3])))

    def test_extract_max_remove_top_element(self):
        """
        extract_max() should remove the top element.
        """
        actual_heap = HeapSort.HeapCapable([5, 4, 3])
        extract_max(actual_heap)
        expected_heap = HeapSort.HeapCapable([4, 3])
        self.assertEqual(expected_heap, actual_heap)

    def test_extract_max_modify_heap_size(self):
        """
        extract_max() should modify the heap_size attribute, not just the array length.
        """
        actual_heap = HeapSort.HeapCapable([5, 4, 3])
        extract_max(actual_heap)
        self.assertEqual(2, actual_heap.heap_size)

    def test_extract_max_general_case(self):
        """
        extract max: general case.
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        extract_max(actual_heap)
        expected_heap = HeapSort.HeapCapable([25, 20, 14, 15, 16])
        self.assertEqual(expected_heap, actual_heap)

    def test_increase_key_middle_element(self):
        """
        increase_key(): general case, increasing the key of an element in the middle of the heap
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        increase_key(actual_heap, 3, 35)
        expected_heap = HeapSort.HeapCapable([35, 27, 25, 16, 15, 20])
        self.assertEqual(expected_heap, actual_heap)

    def test_increase_key_last_element(self):
        """
        increase_key(): general case, increasing the key of the last element in the heap
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        increase_key(actual_heap, 0, 9001)
        expected_heap = HeapSort.HeapCapable([9001, 16, 25, 14, 15, 20])
        self.assertEqual(expected_heap, actual_heap)

    def test_increase_key_invalid_key(self):
        """
        increase_key() should give an error message if the new key is smaller than the existing key.
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        error = increase_key(actual_heap, 0, 24)
        self.assertEqual("new key is smaller than existing key", error)

    def test_insert_large_key(self):
        """
        insert: general case with a large key.
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        insert(actual_heap, 9001)
        expected_heap = HeapSort.HeapCapable([9001, 16, 27, 14, 15, 20, 25])
        self.assertEqual(expected_heap, actual_heap)

    def test_insert_small_key(self):
        """
        insert: general case with a small key.
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        insert(actual_heap, 1)
        expected_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20, 1])
        self.assertEqual(expected_heap, actual_heap)

    def test_insert_middle_key(self):
        """
        insert() should maintain the max-heap property.
        """
        actual_heap = HeapSort.HeapCapable([27, 16, 25, 14, 15, 20])
        insert(actual_heap, 26)
        expected_heap = HeapSort.HeapCapable([27, 16, 26, 14, 15, 20, 25])
        self.assertEqual(expected_heap, actual_heap)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
