def find_all_indices(lst, target):
    return [i for i, val in enumerate(lst) if val == target]
my_list = [3, 5, 2, 3, 7, 3, 9]
target_element = 3

indices = find_all_indices(my_list, target_element)
print(indices)
