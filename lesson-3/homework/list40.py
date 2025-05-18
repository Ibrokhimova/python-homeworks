def unique_in_order(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list
original_list = [3, 5, 3, 2, 5, 1, 2, 4]

result = unique_in_order(original_list)
print(result)
