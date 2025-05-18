my_dict = {'a':5, 'b':10,'c':4, 'd':8}

filtered_dict = {k: v for k, v in my_dict.items() if v > 5}

print("Filteered  dict:", filtered_dict)