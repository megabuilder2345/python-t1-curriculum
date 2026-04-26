import random

# Problem 1  ( 1 : 1 )
# Create a variable for your favorite hobby and print it.
hobby=("LEGOs")
print(hobby)


# Problem 2  ( 1 : 1 )
# Ask the user for a number.
# Print the number multiplied by 3.
user_input1=int(input("gimme a number: "))
print(user_input1 * 3)


# Problem 3  ( 1 : 1 )
# Print every number from 5 to 10 (inclusive) using a for loop.
for i in range(5,11):
    print(i)


# Problem 4  ( 2 : 1 )
# Ask the user for two numbers. 
# Print whether the first is larger, smaller, or equal to the second.
user_input2=int(input("gimme a number: "))
user_input3=int(input("gimme a number: "))
if user_input2 > user_input3:
    print(user_input2)
elif user_input3 > user_input2:
    print(user_input3)
else:
    print("equal")


# Problem 5  ( 2 : 1 )
# Use the modulo operator to print whether a random number from 1 to 20 is divisible by 4.
ran_num=random.randint(1, 20)
if (ran_num % 4)==0:
    print(ran_num, "is divisible by 4")
else:
    print("67")


# Problem 6  ( 2 : 1 )
# Ask the user for a number between 1 and 10.
# Use logical operators to print whether it’s in the lower half (1–5), upper half (6–10) or out of range.
user_input4=int(input("gimme a number between 1 and 67-57: "))
if user_input4 < 6:
    print("lower half")
elif user_input4>4:
    print("upper half")



# Problem 7  ( 2 : 1 )
# Create a list of 5 animals. 
# Print the length of the list and the second animal.
animals=["cheetah", "baer", "dog", "amur leopard", "snow leopard"]
print(len(animals))
print(animals[1])

# Problem 8  ( 3 : 1 )
# Get a random item from the list of colors and print it.
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))


# Problem 9  ( 3 : 2 )
# Ask the user for a number.
# Use a for loop to count how many items in the list of numbers are greater than the user’s number.
numbers = [3, 8, 15, 2, 9, 12]
user_input5=int(input("gimme a number: "))
count = 0
for num in numbers:
    if num > user_input5:
        count += 1
print(count)

# Problem 10  ( 3 : 2 )
# Find the largest number in the list and print it.
numbers = [14, 27, 5, 89, 42]
largest = 0
for num in numbers:
    if num > largest:
        largest = num  
print(largest)


# Problem 11  ( 4 : 2 )
# Write a function that takes two numbers and returns their sum.
# Ask the user for two numbers and use your function to print the result.
user_input6=int(input("gimme a number: "))
user_input7=int(input("gimme a number: "))
print(user_input6 + user_input7)


# Problem 12  ( 4 : 2 )
# Create a global counter starting at 0.
# Write a function that increases it by a random number from 1–5 and prints it.
counter3= 0
def increase_counter():
    global counter3
    increment = random.randint(1, 5)
    counter3+= increment
    print(counter3)
increase_counter()


# Problem 13  ( 5 : 3 )
# Ask the user for a starting number less than 50.
# Use a while loop to add 7 each time until the number is >= 50.
# Print the number at each iteration of the loop.
user_input8 = int(input("Gimme a number less than 50"))
while user_input8<50:
    user_input8 +=7
print(user_input8)


# Problem 14  ( 6 : 3 )
# Create a list of 6 random integers between 1 and 100.
# Print the list, the sum of its numbers, and how many are even.
numbers = []
for i in range(6):
    numbers.append(random.randint(1, 100))
total_sum = sum(numbers)
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(" list:", numbers)
print(" sum:", total_sum)
print("Number of even integers:", even_count)


# Problem 15  ( 7 : 3 )
# Ask the user for 4 words. Store them in a list.
# While the list is not empty:
# - Remove and print the first word.
# - Then print how many words are left.
words = []
for i in range(4):
    word = input("Enter a word: ")
    words.append(word)
print("--- Starting Removal ---")
while len(words) > 0:
    removed_word = words.pop(0)
    print("Removed word:", removed_word)
    print("Words left:", len(words))