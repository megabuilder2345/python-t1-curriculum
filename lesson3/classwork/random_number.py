import random # you must import the random mudule to use random number funtions

num = random.randint(1,10) # picks a random number between 1 and 10 (inclusive0
print(num)

for i in range(1000000):
    num2 = random.randint(1,100)
    print(num2)