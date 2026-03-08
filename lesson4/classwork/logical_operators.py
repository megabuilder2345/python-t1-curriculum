age=int(input("how old are you? "))
has_ticket=input("do you have a movie ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes": # AND: both condition must be true for our code inside the if statement to run 
    print("You can enter the PG-13 movie.")
else:
    print("You cannot enter the PG-13 movie")
print("movie check complete.")

has_pass = input("do you have a pass? (yes/no) ")
has_coins=input("do you have coins to pay? (yes/no) ")

if has_pass == "yes" or has_coins == "yes": # OR: at least one condition must be true for our code inside the if statement to run
    print("you can ride the bus")
else:
    print("you cannot ride the bus")
print("bus check complete.")

homework_done=input("did you do you do your homework? (yes/no) ")
if not homework_done=="yes:" #NOT : flips true to false and false to true
    print("Go finish your homework!")
else:
    print("good job! you're all done.")
print("homework check complete")

#you can combine multiple logical operators
is_raining = input("is it raining? (yes/no) ")
has_umbrella= input("do you have an umbrella? (yes/no) ")

if is_raining== "yes" and not has_umbrella == "yes": #order of operations: first not, than and, then or
    print("stay inside. you might get wet!")
elif is_raining("you're ready to go outside!"):
    print("you're ready to go outside!")
else:
    print("no rain! you can go outside.")