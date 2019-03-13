def get_middle(s):
    if len(s) == 1 or len(s) == 2:
        return s
    elif len(s)%2 == 0:
        l = len(s)/2
        return s[int(l-1):int(l+1)]
    else:
        l = len(s)/2
        return s[int(l-0.5)]

print(get_middle('testing'))

