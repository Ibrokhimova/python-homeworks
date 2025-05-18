my_tuple = (1, 2, 3)
repeat_times = 3

result = ()

for item in my_tuple:
    result += (item,) * repeat_times

print(result)
