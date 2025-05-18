numbers = [10, 40, 20, 50, 30]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers)>=2:
    second_smallest = unique_numbers[1]
    print(second_smallest)
else:
    print("No  second smallest element")
