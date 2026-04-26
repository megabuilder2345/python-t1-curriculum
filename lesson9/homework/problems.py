# Problem 1
# Use a while loop to print the word "Python" 4 times.
i=0
while(i<4):
    print("Python")
    i=i+1



# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
i=2
while(i<14):
    print(i)
    i=i+2


# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
user_input = int(input("Enter a positive number: "))
i = 0

while i <= user_input:
    print(i)
    i += 1



# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
user_input2 = int(input("Enter a number greater than 10: "))
if user_input <= 10:
    print("The number is not greater than 10.")
else:
    current_num = user_input2
    while current_num >= 0:
        print(current_num)
        current_num -= 5

# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals=["cheetah", "snow leopard", "amur leopard"]
i = 0
while i < len(animals):
    print(animals[i] + " is awesome!")
    i += 1