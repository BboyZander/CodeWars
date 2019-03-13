import math

import config
import numpy as np
from modules.timing import elapsed_timer, timeit
np.random.seed(config.seed)


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    a = math.sqrt(sq)
    if int(a) == float(a):
        return int(math.pow(a+1,2))
    else:
        return -1


def find_next_square2(sq):
    root = sq ** 0.5
    if root.is_integer():
        return int((root + 1)**2)
    return -1


# Проверка двух методов на их работоспособность

# @timeit(config.logger, "find_next_square", title=True)
# def foo(numbers):
#     for num in numbers:
#         find_next_square(num)
#
# @timeit(config.logger, "find_next_square2", title=True)
# def foo2(numbers):
#     for num in numbers:
#         find_next_square2(num)
#
#
#
# if __name__ == '__main__':
#     numbers = list(np.random.randint(0, 100000, size=10000))
#     foo(numbers)
#     foo2(numbers)


print(find_next_square(256))
print(find_next_square2(256))
