my_list = [10, 20, 30, 20, 40]
old_value = 20
new_value = 99

if old_value in my_list:
    index = my_list.index(old_value)
    my_list[index] = new_value

print(my_list)
 