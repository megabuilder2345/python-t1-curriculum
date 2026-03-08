age=int(input("how old are you? "))
has_ticket=input("do you have a movie ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes": # AND: both condition must be true for our code inside the if statement to run 
    print("You can enter the PG-13 movie.")
else:
    print("You cannot enter the PG-13 movie")