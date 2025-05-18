
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
target_value = 1
matching_keys = [key for key, value in my_dict.items() if value == target_value]

print(matching_keys)  
