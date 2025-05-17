from datetime import datetime 
name = input("Enter your name:")
b_year = int(input("Enter your year of birth: "))
c_year = datetime.now().year
age = c_year - b_year
print("Result:", age)