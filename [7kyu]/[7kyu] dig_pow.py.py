def dig_pow(n, p):

    left = 0
    for i in str(n):
        left += int(i) ** p
        p += 1
    if int(left/n) == float(left/n):
        res = int(left/n)
        return res
    else:
        return -1


def dig_pow2(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return int(s/n) if s%n==0 else -1

print(dig_pow(695,2))
print(dig_pow2(695,2))