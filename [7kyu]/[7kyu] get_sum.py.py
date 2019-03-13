def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    elif b < a:
        c = 0
        c = a
        a = b
        b = c
        l = []
        for i in range(a,b+1):
            l.append(i)
        return sum(l)
    else:
        l = []
        for i in range(a,b+1):
            l.append(i)
        return sum(l)

print(get_sum(0,-1))