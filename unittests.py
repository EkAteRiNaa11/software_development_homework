"""
Рожнова Екатерина Александровна
Группа 44-22-112
Вариант 21
"""


import unittest
from expression import expression
import numpy as np


class TestExpression(unittest.TestCase):
    def test_equal(self):
        # использовать np.allclose нужно,
        # т.к. калькулятор не выводит столько знаков
        # после запятой, как python.
        # и иногда может произвольно округлять/не округлять
        # последний знак
        self.assertTrue(
            np.allclose(
                np.array(expression(1, 2, 3, 4, 5)[0]),
                np.array([
                    -0.17260374626,
                    0.59806414446,
                    3.16227766017,
                    3.31662479036,
                    3.46410161514
                ])
            )   
        )

    def test_nan(self):
        self.assertFalse(bool(expression(0)[0][0]))
        self.assertFalse(bool(expression("Hello, world!")[0][0]))
        self.assertFalse(bool(expression(None)[0][0]))


if __name__ == "__main__":
    unittest.main()