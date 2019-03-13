import config
import numpy as np
from modules.timing import elapsed_timer, timeit
np.random.seed(config.seed)

def expanded_form(num):
    res = str(num)
    mas = []
    for item, idx in zip(res, reversed(range(len(str(num))))):
        if item == '0':
            continue
        mas.append(item + '0'*idx)
    return ' + '.join(mas)


def expanded_form2(num):
    return ' + '.join([x+i*'0' for x,i in zip(str(num),reversed(range(len(str(num))))) if x != '0'])


@timeit(config.logger, "expanding form", title=True)
def foo(numbers):
    for num in numbers:
        expanded_form(num)

@timeit(config.logger, "expanding form2", title=True)
def foo2(numbers):
    for num in numbers:
        expanded_form2(num)



if __name__ == '__main__':
    numbers = list(np.random.randint(0, 100000, size=1000))
    foo(numbers)
    foo2(numbers)
