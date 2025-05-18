numbers = [10,15,22,33,40,90,55]
odd_count = sum(1 for num in numbers if num % 2 != 0)
print("Odd count:",odd_count)
