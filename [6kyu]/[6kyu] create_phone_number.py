# Функция, которая записывает номер телефона в определенном формате

def create_phone_number(n):
    m = [str(i) for i in n]
    elements = [m[:3],m[3:6],m[6:]]
    first = '(' + ''.join(elements[0]) + ') '
    second = ''.join(elements[1])+'-'
    third = ''.join(elements[2])
    return first + second + third

def create_phone_number2(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(create_phone_number2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
