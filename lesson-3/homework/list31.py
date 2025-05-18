original_list = [1,2,3]
repeat_count = 3
repeated_list = [elem for elem in original_list for _ in range(repeat_count)]

print(repeated_list)