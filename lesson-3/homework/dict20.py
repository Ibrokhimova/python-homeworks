my_dict = {'c':3, 'a':1,'b':2}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print("Sorted dict:", sorted_dict)