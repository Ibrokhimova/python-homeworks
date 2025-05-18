def create_nested_list(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst), n)]
original_list = [1,2,3,4,5,6,7,8]
chunk_size = 3
nested_list = create_nested_list(original_list, chunk_size)
print(nested_list)