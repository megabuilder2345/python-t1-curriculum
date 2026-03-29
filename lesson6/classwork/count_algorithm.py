numbers = [14, 1, 50, 4, 20, 12]

counter = 0 # keep track of how many numbers so far in my list are greater than 5

for i in range(len(numbers)): # looping through the list  of numbers using an index
    item = numbers[i] # get the current item which we are on in the list
    if item > 5: #check if the current item is greater than 10
        counter=counter + 1 # if it is greater than 5, add 1 to the counter
print("there are", counter, "numbers greater than 5 in our list")

animals = ["cat","dog","cat", "rabbit", "cat"]

counter2 = 0 # keeps track of how many times we see "cat" in our list

for i in range(len(animals)):
    item = animals[i] # get the current item which we are on in the list
    if item == "cat":
        counter2 = counter2 +1 # if it is "cat", add 1 to the counter

if found ==True:
    print("found apple at index", index)
else:
    print("no apples in list")