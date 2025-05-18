my_tuple = (4,3,2,6,8,9)
unique_elements =list(set(my_tuple))
if len(unique_elements)<2:
    second_smallest =None
else:
    unique_elements.sort()
    second_smallest = unique_elements[1]
print("Second smallest:", second_smallest)    