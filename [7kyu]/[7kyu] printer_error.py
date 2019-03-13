import string

def printer_error(s):
    s = s.lower()
    length = len(s)
    good_colors = string.ascii_lowercase[:13]
    error = [v for v in s if v not in good_colors]
    return str(len(error))+'/'+str(length)

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))