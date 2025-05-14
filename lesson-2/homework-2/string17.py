str = input("Enter a string:")
vowel = "aeiouAEIOU"
rep_tex = ''.join('*' if char in vowel else char for char in str)
print("Vowels replaced:", rep_tex)