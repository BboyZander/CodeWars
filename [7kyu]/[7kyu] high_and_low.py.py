def high_and_low(numbers):
    mas = []
    for l in numbers.split():
        mas.append(int(l))

    return str(max(mas)) + ' ' + str(min(mas))


print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))
