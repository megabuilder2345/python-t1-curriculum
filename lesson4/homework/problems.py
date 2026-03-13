# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
user_input=int(input("what was your test score "))
user_inpu2=int(input("what was your other test score "))
if user_input >= 50 and user_inpu2 >=50:
    print("You passed both!")
else:
    print("you failed at least one.")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
user_input3=input("did you buy water? (yes/no) ")
user_input4=input("did you buy lunch? (yes/no) ")
if user_input3=="yes" and user_input4 == "yes":
    print("You're fully ready!")
elif user_input4 == "yes" or user_input3=="yes":
    print("you're somewhat ready.")
else:
    print("You're not ready.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_input5=int(input("pick a number: "))
if user_input5<11 or user_input5>0:
    print("in range")
else:
    print("out of range")


# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num = random.randint(1,10)
user_input6=int(input("guess a number from 1 to 10"))
if num==user_input6 and num % 2==0:
    print("Even match!")
elif num==5 or num==user_input6:
    print("nice try!")
else:
    print("nope")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
user_input7=int(input("give me a number"))
user_input8=int(input("give me a number"))
if (user_input7 % 5==0 and user_input8 % 2!=0) or (user_input7 % 5==0 and user_input7 % 2!=0):
    print("Interesting pair!")
else:
    print("plain pair")