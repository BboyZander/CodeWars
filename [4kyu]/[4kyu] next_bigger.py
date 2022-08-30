import time

def next_bigger(n):
    # create a list representation of the input integer
    arr = list(str(n))
    
    # sort in reverse to get the largest possible number
    max_n = int("".join(sorted(arr, reverse=True)))
    
    # sort to get the minimum number
    min_n = sorted(arr)
    
    # copy the input to a new variable
    m = n
    
    # loop while less than or equal to the max
    while m <= max_n:
        # increment our number
        m += 1
        # if found in our min list
        if sorted(list(str(m))) == min_n:
            # return the new number
            return m
        
    # if all else fails, return -1
    return -1

if __name__ == '__main__':
    start_time = time.time()
    
    next_bigger(123)
    print("--- %s seconds ---" % (time.time() - start_time))

