def sum_nested_numbers(a, index = 1) :
    total = 0
    for item in a :
        try:
            total += item**index
        except TypeError:
            total += sum_nested_numbers(item, index+1)
    return total