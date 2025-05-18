def is_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    if sub_len == 0:
        return True
    return any(main_list[i:i+sub_len] == sub_list for i in range(len(main_list) - sub_len + 1))

main = [1, 2, 3, 8, 7]
sub = [7, 9, 34]

print(is_sublist(main, sub))  
