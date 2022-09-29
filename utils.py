import random
import sys


def написать(*args) -> None:
    args_ = str([arg for arg in args])
    sys.stdout.write(args_[1:-1:])


def число(number: int) -> int:
    return int(number)


def строка(striing: str) -> str:
    return str(striing)


def рандом_рандинт(first: int, second: int) -> int:
    return random.randint(first, second)


def список(*args, **kwargs) -> list:
    if args and kwargs:
        args_ = [arg for arg in args]
        kwargs_ = [kwarg for kwarg in kwargs.values()]
        return args_ + kwargs_
    return list()
