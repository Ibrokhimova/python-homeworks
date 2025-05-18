my_tuple=(1,2,3,2,4,5)
element_to_remove = 2
result =()
removed = False
for item in my_tuple:
    if  item == element_to_remove and not removed:
        removed = True
        continue
    result+=(item,)
print(result)    