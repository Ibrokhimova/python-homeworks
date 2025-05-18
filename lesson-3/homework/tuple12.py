my_tuple = (4,3,2,6,8,9)
unique_elements =list(set(my_tuple))
if len(unique_elements)<2:
    secondl_largest =None
else:
    unique_elements.sort()
    second_largest = unique_elements[-2]
print("Secong largest:", second_largest)    