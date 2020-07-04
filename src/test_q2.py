import unittest
import numpy as np

from q2 import recurrence_relation_elements, CharactersABC, ABCCounter


class TestQ2(unittest.TestCase):
    def test_recurrence_relation_elements(self):
        xs = list(range(10))
        for i in range(0, len(xs)-3):
            expectation = xs[i:i+3]
            actual = list(reversed(recurrence_relation_elements(i + 3)))
            with self.subTest(expectation=expectation, actual=actual):
                np.testing.assert_equal(expectation, actual)

    def test_charactersabc_clear(self):
        char_abc = CharactersABC()
        abc = [10, 11, 12]
        char_abc.a = abc[0]
        char_abc.b = abc[1]
        char_abc.c = abc[2]
        self.assertEqual((char_abc.a, char_abc.b, char_abc.c),
                         tuple(abc))
        char_abc.clear()
        actual = (char_abc.a, char_abc.b, char_abc.c)
        expectation = (0, 0, 0)
        self.assertEqual(actual, expectation)

    def test_charactersabc_add(self):
        char_abc = CharactersABC()
        expectation = (10, 11, 12)
        char_abc.add(*expectation)
        actual = (char_abc.a, char_abc.b, char_abc.c)
        self.assertEqual(actual, expectation)

    def test_charactersabc_abc(self):
        char_abc = CharactersABC()
        abc = [10, 11, 12]
        char_abc.a = abc[0]
        char_abc.b = abc[1]
        char_abc.c = abc[2]
        actual = char_abc.abc
        expectation = tuple(abc)
        self.assertEqual(actual, expectation)

    def test_recurrence_relation_elements_string(self):
        S = _test_stacked_strings(5)  # ['a', 'b', 'c', 'abc', 'bcabc']
        k = 4
        ks = reversed(recurrence_relation_elements(k - 1))
        actual = _stack_test_string(ks, S)
        self.assertEqual(S[k-1], actual)

        k = 5
        ks = reversed(recurrence_relation_elements(k - 1))
        actual = _stack_test_string(ks, S)
        self.assertEqual(S[k-1], actual)

    def test_make_abc_counts(self):
        k = 25
        abc_counter = ABCCounter()
        abc_counter.update(k)
        actuals = abc_counter.counts
        expectations = _create_test_abc_counts(k)
        for expectation, actual in zip(expectations, actuals):
            self.assertEqual(expectation, actual)

    def test_search_abc_counts(self):
        k = 25
        strings = _test_stacked_strings(k)
        abc_counts = _create_test_abc_counts(k)
        abc_counter = ABCCounter()
        abc_counter.counts = abc_counts
        for i, string in enumerate(strings):
            if len(string) == 1:
                p = 1
                q = 1
            else:
                p, q = sorted(np.random.choice(np.arange(1, len(string) + 1),
                              2, replace=False))

            with self.subTest(k=i+1, p=p, q=q, string=string):
                # p-1は0-indexにするため
                expectation = _test_count_abc(string[p-1:q])
                actual = abc_counter.search(i + 1, p, q)
                self.assertEqual(expectation, actual)


def _stack_test_string(ks, strings):
    k1, k2, k3 = ks
    return strings[k1] + strings[k2] + strings[k3]


def _test_stacked_strings(k):
    strings = ["a", "b", "c"]
    for i in range(3, k):
        strings.append(_stack_test_string((i - 3, i - 2, i - 1), strings))
    return strings


def _create_test_abc_counts(k):
    abc_counts = []
    strings = _test_stacked_strings(k)
    for string in strings:
        count = _test_count_abc(string)
        abc_counts.append(count)
    return abc_counts


def _test_count_abc(string):
    a = string.count("a")
    b = string.count("b")
    c = string.count("c")
    return a, b, c


if __name__ == "__main__":
    unittest.main()
