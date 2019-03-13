def compute_depth(n, it = 1):
    ethalon = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    res = set()
    while sorted(res) != sorted(ethalon):
        num = n*it
        for i in str(num):
            if i not in res:
                res.add(int(i))
        it += 1

    return it-1

print(compute_depth(1))

def compute_depth2(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i