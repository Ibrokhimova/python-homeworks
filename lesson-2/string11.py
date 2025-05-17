x = input("Enter a sentence:")
digit = any(char.isdigit() for char in x)
if digit:
    print("it contains digit")
else:
    print("it does not contain any digit")