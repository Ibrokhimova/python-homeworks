my_dict = {'a':3, 'b':1,'c':2}

sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

print("Sorted dict:", sorted_dict)