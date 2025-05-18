
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd':3}
value_to_count = 1

count = list(my_dict.values()).count(value_to_count)

print(f"The value {value_to_count} appears {count} time(s).")

