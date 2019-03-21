def sort_array(source_array):
    # Return a sorted array.
    odd_numbers = [(i, v) for i, v in enumerate(source_array) if v%2 != 0]
    sorted_odds = sorted(odd_numbers, key=lambda x: x[1])
    new_odds = [v[1] for v in sorted_odds]
    new_index = sorted([v[0] for v in sorted_odds])
    for i, v in zip(new_index, new_odds):
        source_array[i] = v
    return source_array

# clever try
def sort_array_2(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

print(sort_array([5, 3, 2, 8, 1, 4, 0]))