import re

def count_smileys(text):
    word = ''
    for i in text:
        word += i + ' '
    return len(re.findall('[:;][-~]?[)D]', word))

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))