"""
Timing function I found from StackExchange answer:
https://codereview.stackexchange.com/questions/169870/decorator-to-measure-execution-time-of-a-function

"""

from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f"Elapsed time: {end - start}")
        return result

    return wrapper
