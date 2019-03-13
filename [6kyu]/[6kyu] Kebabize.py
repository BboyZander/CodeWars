
def kebabize(string):
    res = ''
    for i in string:
        if i.isdigit():
            continue
        elif i == i.upper():
            res += '-' + i.lower()
        else:
            res += i
    #your code here
    return res.lstrip('-')


def kebabize2(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')


print(kebabize('HelloMo234therFucker'))
print(kebabize2('HelloMo234therFucker'))