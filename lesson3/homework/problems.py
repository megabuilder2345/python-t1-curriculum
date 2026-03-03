# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input=input("give me an integer: ")
b=2
number=int(user_input)


#(number - (b * (number//b)))
remainder=(number - (b * (number//b)))
if remainder==0:
    print("even")
elif remainder==1:
    print("odd")
print("")

# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
user_input4=input("what day of the week is it: ")
if user_input4=="saturday":
    print("Weekend")
elif user_input4=="sunday":
    print("Weekend")
else:
    print("Weekday")
print("")




# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".

# we have not covered this yet

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
number4=10
user_input3=input("give me an integer: ")
number3=int(user_input3)
if remainder==0:
    if number3 > number4:
        print("Big even number")
elif remainder==1:
    print("Number does not meet criteria")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
print("")
user_input1 = input("give me an interger:")
user_input2 = input("give me an interger:")
number1 = int(user_input1)
number2 = int(user_input2)
if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
elif number2==number1:
    print("Numbers are equal")