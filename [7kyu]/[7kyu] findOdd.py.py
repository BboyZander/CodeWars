def find_it(seq):
    for i, val in enumerate(seq):
        if seq.count(val)%2 != 0:
            return seq[i]

print(find_it([1,1,1,2,2]))
