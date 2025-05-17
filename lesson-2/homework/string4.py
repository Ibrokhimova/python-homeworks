t = input("Enter a string:")
c_t = t.replace("","").lower()
if c_t == c_t[::-1]:
    print("it's palindrome")
else:
    print("it's not a palindrome")