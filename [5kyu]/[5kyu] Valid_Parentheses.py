def valid_parentheses(row):
    import re
    from collections import Counter

    pattern = "[](){}[]+"
    row_filtered = ''.join(re.findall(pattern, row))

    while '()' in row_filtered:
        row_filtered = row_filtered.replace('()', '')
    if len(row_filtered) > 0:
        return False
    else:
        return True
