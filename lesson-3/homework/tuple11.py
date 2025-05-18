def get_all_indices(tpl, element):
    return [i for i, val in enumerate(tpl) if val == element]
my_tuple = (1, 2, 3, 2, 4, 2, 5)
element = 2

indices = get_all_indices(my_tuple, element)
print(indices)
