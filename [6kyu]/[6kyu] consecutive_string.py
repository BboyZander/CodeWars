
def longest_consec(s, k):

    if len(s) == 0 or k > len(s) or k <= 0:
        return ''
    else:
        return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len)

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"],2))
print(longest_consec(["aaa","bbbb","ccc"], 2))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))