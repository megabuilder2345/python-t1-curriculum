fruits=["apple", "banana", "cherry"]

#find if apple is in the list
if "apple" in fruits:
    print("found apple")
else:
    print("apple not found")

found = False
index = -1

for i in range(len(fruits)): # looping through the list
    if fruits[i] == "apple": # checking if the current Item is apple
        found=True # mark as found
        index = i # store the index whre we found an apple
        break # exit the loop since we found the apple

if found ==True:
    print("found apple")
else:
    print("no apples in list.")