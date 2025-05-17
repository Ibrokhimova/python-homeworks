txt = 'LMaasleitbtui'
txt_lower = txt.lower()
cars = ['audi','kia', 'bmw', 'tesla', 'nexia']
f_cars = [car for car in cars if car in txt_lower]
print(f_cars)