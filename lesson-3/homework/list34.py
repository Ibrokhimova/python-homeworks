def rotate_list_right(lst,k):
    if not lst:
        return[]
    k=k%len(lst)
    return lst[-k:]+lst[:-k]
original_list =[1,2,3,4,5]
k = 2
rotated = rotate_list_right(original_list, k)
print(rotated)