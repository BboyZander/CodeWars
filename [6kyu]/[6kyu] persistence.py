import re

def persistence(n):
    ia = 0
    r = 1
    for i in re.findall(r'\d{1}', str(n)):
        r *= int(i)
    ia += 1
    persistence(r)
    return ia

print(persistence(123))
