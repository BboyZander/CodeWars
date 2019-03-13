def find_uniq(arr):
    # your code here
    if arr.count(list(set(arr))[0]) > arr.count(list(set(arr))[1]):
        return list(set(arr))[1]
    else:
        return list(set(arr))[0]
   # n: unique integer in the array

print(find_uniq([1,1,1,1,2,1]))