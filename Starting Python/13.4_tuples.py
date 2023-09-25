# Tuples are like list, nut immutable, no one can mutate or change them.
n = (1, 2, 3, 2) # [..., ..., ..., ...] -> define lists, (..., ..., ..., ...) -> define tuples

# if you try -> n[0] = 4 it will return a error message

# Tuples don't have insert methods, so we can't add new items and another things
# The only two methods we can use in a Tuple -> 'count' and 'index'

print(n.count(2)) # count the number of occurrences of an item
print(n.index(3)) # return the index of the first occurrence of an item