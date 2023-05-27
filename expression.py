"""
Рожнова Екатерина Александровна
Группа 44-22-112
Вариант 21
"""

import math
import sys
from pprint import pprint


def expression(*args):
    """
    args -> список x-ов для выражения
    """

    def safely_parse(string: str):
        """
        если строку можно превратить в дробь
        то вернуть дробь,
        иначе вернуть None
        """
        try:
            return float(string)
        except:
            return None

    def function1(x: float):
        """
        Функция для случаев, когда
        x <= 2
        """
        try:
            return math.log(abs(x * math.sin(x)))
        except:
            return None

    def function2(x: float):
        """
        Функция для случаев, когда
        x > 2
        """
        try:
            return math.sqrt(x + 7)
        except:
            return None
    
    # Функция должна вернуть вычисленные значения
    # для каждого входного х
    return_values = []
    log_values = []
    for x_orig, x in zip(args, map(safely_parse, args)):
        # Если число - не дробь, то вернуть None
        if x is None:
            return_values.append(None)
            log_values.append(f"{x_orig} -> {x} -> None")
            continue
        
        # Иначе вычислить функцию
        if x <= 2:
            fx = function1(x)
        else:
            fx = function2(x)
        
        log_values.append(
            f"{x_orig} -> ln|{x} * sin({x})| = {fx}"
            if x <= 2
            else f"{x_orig} -> sqrt({x} + 7) = {fx}"
        )
        return_values.append(fx)
    
    pprint(log_values)
    return return_values, log_values


if __name__ == "__main__":
    # Файл можно запускать из командной строки
    # с произвольным количеством аргументов
    expression(*sys.argv[1:])