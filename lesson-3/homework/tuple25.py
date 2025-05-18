my_tuple = (2, 4, 2, 5, 4, 7, 5)
unique_elements = ()
seen = set()

for item in my_tuple:
    if item not in seen:
        unique_elements += (item,)
        seen.add(item)

print(unique_elements)
