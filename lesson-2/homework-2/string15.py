sent = input("Enter a string:")
x = ''.join(word[0].upper() for word in sent.split())
print("Result:", x)