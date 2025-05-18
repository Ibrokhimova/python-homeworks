my_list = [5,12,10,15,17,3]
index_to_remove = 2
if 0<=index_to_remove<len(my_list):
    removed_element = my_list.pop(index_to_remove)
    print(f"Removed element: {removed_element}")
else:
    print("Invalid index.")

print("Updated list:", my_list)
