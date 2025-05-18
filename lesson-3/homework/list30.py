def is_sorted(lst):
    return lst == sorted(lst)
print(is_sorted([1,2,3,4,5]))
print(is_sorted([5,4,3,2,1]))