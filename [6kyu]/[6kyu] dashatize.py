def dashatize(num):

    if not num and not (num == 0):
        return 'None'
    a = str(abs(num))
    res = ''

    for char in a:
            if int(char)%2 != 0:
                res += '-' + char + '-'
            else:
                res += char
    return res.strip('-').replace('--','-')


print(dashatize(-12312223))