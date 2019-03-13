def accum(s):
    count = 0
    count2 = 0
    k = len(s)
    res = ''
    for i in range(len(s)):
        res +=s[count].capitalize()
        for z in range(count2):
            res += s[count].lower()
        count2 += 1
        count += 1
        if k > 1:
            res += '-'
            k -= 1
    return res


print(accum('asda'))

"""
Вариант в одну строчку

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

"""