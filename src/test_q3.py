import unittest
import heapq

from q3 import (center_left_index, side_length, SeatingArrangement, sum_even)


class TestQ3(unittest.TestCase):
    def test_center_left_index(self):
        expectations = [0, 0, 1, 1, 2, 2, 3]
        for i, expectation in enumerate(expectations):
            with self.subTest(length=i+1):
                actual = center_left_index(i+1)
                self.assertEqual(expectation, actual)

    def test_side_length(self):
        expectations = [(0, 4), (1, 3), (2, 1), (1, 1),
                        (0, 0), (0, 4), (1, 3)]  # (left, right)
        indexes = [(1, 1, 5), (1, 2, 5), (2, 4, 4), (3, 4, 3),
                   (5, 5, 1), (0, 0, 5), (0, 1, 5)]  # (first, split, length)
        for ((first_index, split_index, length),
             expectation) in zip(indexes, expectations):
            with self.subTest(first_index=first_index,
                              split_index=split_index):
                actual = side_length(first_index, split_index, length)
                self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_5_elements_01(self):
        expectation = [1, 5, 3, 2, 4]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(5, 1)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_5_elements_02(self):
        expectation = [2, 5, 3, 1, 4]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(5, 2)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_5_elements_03(self):
        expectation = [3, 1, 5, 2, 4]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(5, 3)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_5_elements_04(self):
        expectation = [4, 1, 2, 3, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(5, 4)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_5_elements_05(self):
        expectation = [5, 1, 3, 2, 4]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(5, 5)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_01(self):
        expectation = [1, 6, 3, 4, 2, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 1)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_02(self):
        expectation = [2, 6, 4, 1, 3, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 2)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_03(self):
        expectation = [3, 6, 1, 4, 2, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 3)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_04(self):
        expectation = [4, 1, 6, 2, 3, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 4)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_05(self):
        expectation = [5, 1, 3, 2, 4, 6]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 5)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_6_elements_06(self):
        expectation = [6, 1, 3, 4, 2, 5]
        sa = SeatingArrangement(first_index=1)
        actual = sa.search(6, 6)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement_searcht_frist_0_indexes(self):
        max_length = 10
        a = 4
        sa_0 = SeatingArrangement(first_index=0)
        actual = sa_0.search(max_length, a - 1)
        sa_1 = SeatingArrangement(first_index=1)
        expectation = list(map(lambda x: x - 1, sa_1.search(max_length, a)))
        self.assertEqual(expectation, actual)

    def test_seating_arrangement__select_seat_left_odd_length(self):
        sa = SeatingArrangement(first_index=1)
        length = 6
        index = 2
        sa.seats_left = [(-length, index)]
        actual = sa._select_seat(10)
        expectation = (center_left_index(length) + index, index, length)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement__select_seat_left_even_length(self):
        sa = SeatingArrangement(first_index=1)
        length = 6
        index = 2
        sa.seats_left = [(-length, index)]
        actual = sa._select_seat(10)
        expectation = (center_left_index(length) + index, index, length)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement__select_seat_left_length_longer(self):
        sa = SeatingArrangement(first_index=1)
        length = 7
        index = 4
        sa.seats_left = [(-6, 3), (-5, 2),
                         (-length, index), (-5, 5)]
        heapq.heapify(sa.seats_left)
        actual = sa._select_seat(30)
        expectation = (center_left_index(length) + index, index, length)
        self.assertEqual(expectation, actual)

    def test_seating_arrangement__select_seat_left_putting_left_length(self):
        sa = SeatingArrangement(first_index=1)
        length = 3
        index = 2
        sa.seats_left = [(-length, 3), (-length, index),
                         (-length, 4), (-length, 5)]
        heapq.heapify(sa.seats_left)
        actual = sa._select_seat(20)
        expectation = (center_left_index(length) + index, index, length)
        self.assertEqual(expectation, actual)

    def test_sum_even(self):
        x = [1, 2, 3, 4, 5]
        actual = sum_even(x)
        expectation = 6
        self.assertEqual(expectation, actual)


if __name__ == "__main__":
    unittest.main()
