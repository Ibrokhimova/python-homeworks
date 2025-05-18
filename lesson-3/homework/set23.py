import random

n = 5          
start = 1       
end = 20       
random_set = set()
while len(random_set) < n:
    random_set.add(random.randint(start, end))

print(random_set)
