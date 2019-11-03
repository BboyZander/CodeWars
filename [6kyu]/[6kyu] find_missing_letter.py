import string
import numpy as np

def find_missing_letter(chars):
    chars_ = [x.lower() for x in chars]
    if chars == chars_:
        d = {ch: n + 1 for n, ch in enumerate(string.ascii_lowercase)}
    else:
        d = {ch: n + 1 for n, ch in enumerate(string.ascii_uppercase)}

    inv_d = {v: k for k, v in d.items()}

    numbers = [d[x] for x in chars]
    minmax = np.arange(min(numbers), max(numbers)+1)
    idx = [i for i in minmax if i not in numbers]

    return inv_d[idx[0]]

print(find_missing_letter(['a','b','c','d','f']))

