def calculate_years(principal, interest, tax, desired):
    i = 0
    while principal < desired:
        add = principal * interest * (1 - tax)
        principal += add
        i+=1

    return i


print(calculate_years(1000,0.01625,0.18,1200))