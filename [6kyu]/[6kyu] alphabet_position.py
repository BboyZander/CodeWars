import string
import re

def alphabet_position(text):
    text = text.lower()
    d = {ch: n + 1 for n, ch in enumerate(string.ascii_lowercase)}
    regexp = r"[a-z]"

    splitter = re.findall(regexp, text)
    numbers = [str(d[x]) for x in splitter]
    return " ".join(numbers)


print(alphabet_position("The sunset sets at twelve o' clock."))