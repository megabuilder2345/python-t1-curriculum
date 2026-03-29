numbers=[5,-8,35,-3,6,2]

total = sum(numbers) # shortcut to find sum
print("the sum is:", total)

print("our algorithim")

total2=0
for i in range(len(numbeeres)): #go through each index in the list
    item = numbers[i] # get the number at the current index
    total2=total2 + item # add the current number to the total
print("The sum is:", total2)

# find the sum of onlz the positive numbers.

total3=0
for i in range(len(numbers)): # get through each index in the list
    item=numbers[i]
    if item>0: #check if the current number is positive
        total3 = total3 +item # add the current number to the running total if it is positive
print("The sum of onl the positive numbers is:", total3)