def duplicate_count(text):
    # Your code goes here
    low_text = text.lower()
    res = 0
    for i in low_text:
        if low_text.count(i) > 1:
            res += 1
            low_text = low_text.replace(i, '')
    return res

print(duplicate_count('indivisibility'))