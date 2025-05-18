numbers = [10, 40, 20, 50, 30]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers)>=2:
    second_largest = unique_numbers[1]
    print(second_largest)
else:
    print("No  second largest element")
