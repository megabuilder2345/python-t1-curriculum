numbers=[1,2,3,4,5,6]
print(numbers)

# you can use built in python funtions to find the biggest and smallest numbers in a list
biggest_item=max(numbers)
smallest_item=min(numbers)

print("the biggest item in the list is:", biggest_item)
print("the smallest item in the list is:", smallest_item)

print("our algorithim:")

biggest =  numbers[0] #start bz assuming the first item is the biggest
for i in range(len(numbers)): #go through each item in the list
    if numbers[i] > biggest: # check if the current item is bigger than the bigger item wev'e seen so far
        biggest =numbers[i] #if we find a bigger item, update biggest to that item
print("the biggest item in the list is:", biggest) 