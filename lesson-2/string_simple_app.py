"""
name =  "John" #("What is your name? ")
age =   30 #int(input("Age: "))
print(f"Your name is {name} and you are {age} years old.")
print("Your name is {fname}and you are {Age} years old.".format(Age=age, fname=name))
print("Your name is {} and you are {} years old..".format(name,age))
"""
 # + stringar uchun "concatenation"
 
#n = 3486794
#print(f"{n:5f}")
#print(n)
#name1="Adam"
#name2 = "John"
#print(f"{name1:<8} - first name")
#print(f"{name2:<20} - second name")
#my_str= "Hello World" #Sequence 
#print(len(my_str))
#slicing or indexing
#print(my_str[0:2])
#print(my_str[:4]+my_str[5:])
#print(my_str[::2])
#print(my_str[-2])
#SyntaxError
#TypeError
#ValueError
#IndexError
#word = "Apple" #input("Word:")
#last_character = word[len(word)-1]
#print(f"Last character is :{last_character}")
#print("Last character is: ", last_character, )
 

 #Mutable vs Immutable(ozgaruvchan ozgarmas)
#my_text = "Apple"
#print("oldin:", id(my_text))
#my_text = 'a'+my_text[1:]
#print("keyin", id(my_text)) 

#case Sensentitive 
fruit = "Apple banana"
print(fruit.lower())
print(fruit.upper())
print(fruit.capitalize())
print(fruit.title())
print(fruit.endswith('b'))
print(fruit.startswith('b'))


word = '               hello world   '
print(word)
print(word.strip())

fruits = 'apple banana cherry'
print(fruits.split())
file_name = "numaric.py"
base_name = file_name.split(',')[0]
Exception = file_name.split(','[1])
print(f"{file_name=}")
print(f"{base_name=}")
print(f"{Exception=}")
