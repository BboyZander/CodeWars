import config
import numpy as np
from modules.timing import elapsed_timer, timeit
np.random.seed(config.seed)

def find(n):
    mas = []
    res = 0
    for i in range(n+1):
        if i%3 == 0 or i%5 == 0:
            mas.append(i)

    for i in mas:
        res += i

    return res


def find2(n):

    return sum([i for i in range(n+1) if i % 3 == 0 or 0 == i % 5])


# @timeit(config.logger, "find", title=True)
# def foo(numbers):
#     for num in numbers:
#         find(num)
#
# @timeit(config.logger, "find2", title=True)
# def foo2(numbers):
#     for num in numbers:
#         find2(num)
#
#
#
# if __name__ == '__main__':
#     numbers = list(np.random.randint(0, 100000, size=1000))
#     foo(numbers)
#     foo2(numbers)


print(find(10))
print(find2(10))

a = 'TTATG'
b = a.replace('T','C')
print(b)