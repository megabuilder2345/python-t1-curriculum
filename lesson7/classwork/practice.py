# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]

total=sum(numbers)
print(total)

# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]

biggest=max(numbers)
print(numbers)

# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]

total=0
for i in range(len(numbers)):
    item = numbers[i]
    if item <0:
        total = total+item
print(total)

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]

for i in range(len(numbers)):
    item =numbers[i]
    if item %2==0:
        total=total+item

# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]

biggest = -9999
for i in range(len(numbers)):
    item=numbers[i]
    if item <0 and item > biggest:
        biggest = item