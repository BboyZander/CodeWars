def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

def is_isogram2(string):
    return len(string) == len(set(string.lower()))

