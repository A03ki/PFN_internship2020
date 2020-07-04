import unittest
import numpy as np
from collections import Counter

from q1 import (fill_squares, count_matching_determinant,
                count_matching_determinant_filled)


class TestQ1(unittest.TestCase):
    def test_fill_squares_4elements(self):
        for i in range(1, 10):
            data = np.random.randint(-10, 10, i)
            expectation = _create_test_filled_squares_4elements(data)
            actual = fill_squares(data, 2)
            np.testing.assert_equal(expectation, actual)

    def test_fill_squares_9elements(self):
        for i in range(1, 4):
            data = np.random.randint(-10, 10, i)
            expectation = _create_test_filled_squares_9elements(data)
            actual = fill_squares(data, 3)
            np.testing.assert_equal(expectation, actual)

    def test_count_matching_determinant_4elements(self):
        n = 2
        array = np.random.randint(-10, 10, (100, n, n))
        ds = _create_test_determinants(array)

        for d, count in Counter(ds).items():
            with self.subTest(d=d):
                actual = count_matching_determinant(array, d)
                self.assertEqual(count, actual)

    def test_count_matching_determinant_9elements(self):
        n = 3
        array = np.random.randint(-10, 10, (100, n, n))
        ds = _create_test_determinants(array)

        for d, count in Counter(ds).items():
            with self.subTest(d=d):
                actual = count_matching_determinant(array, d)
                self.assertEqual(count, actual)

    def test_count_matching_determinant_filled(self):
        x, y = np.random.randint(-10, 10, 2)
        array = _create_test_filled_squares_9elements([x, y])
        ds = _create_test_determinants(array)

        for d, count in Counter(ds).items():
            with self.subTest(d=d):
                actual = count_matching_determinant_filled(x, y, d)
                self.assertEqual(count, actual)


def _create_test_determinants(array):
    "array: 三次元配列"
    ds = [None] * len(array)
    for i in range(len(array)):
        w, _ = np.linalg.eig(array[i])
        ds[i] = np.round(np.product(w))
    return ds


def _create_test_filled_squares_4elements(data):
    x = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                for m in range(len(data)):
                    x.append([data[i], data[j], data[k], data[m]])
    return np.array(x).reshape(-1, 2, 2)


def _create_test_filled_squares_9elements(data):
    x = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                for m in range(len(data)):
                    for n in range(len(data)):
                        for o in range(len(data)):
                            for p in range(len(data)):
                                for q in range(len(data)):
                                    for r in range(len(data)):
                                        x.append([data[i], data[j],
                                                  data[k], data[m],
                                                  data[n], data[o],
                                                  data[p], data[q],
                                                  data[r]])
    return np.array(x).reshape(-1, 3, 3)


if __name__ == "__main__":
    unittest.main()
