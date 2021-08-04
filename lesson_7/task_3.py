from typing import Literal


def make_operation(operation: Literal["+", "-", "*"], *args) -> int:
    if operation == "+":
        return sum(args)

    if operation == "-":
        result = 0
        for num in args:
            result -= num
    else:
        result = 1
        for num in args:
            result *= num

    return result


