def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order('AAAABBBCCDAABBB'))