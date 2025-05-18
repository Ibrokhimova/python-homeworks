def get_middle_elements(lst):
    n = len(lst)
    mid = n // 2
    if n == 0:
        return None  
    if n % 2 == 1:
        return lst[mid]
    else:
        return lst[mid-1:mid+1]
print(get_middle_elements([1, 2, 3, 4, 5]))      
print(get_middle_elements([1, 2, 3, 4, 5, 6]))   
print(get_middle_elements([]))                   

