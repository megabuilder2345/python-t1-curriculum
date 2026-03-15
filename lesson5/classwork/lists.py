# A list is, apple, banana, orange, etc..............
#apple, banana, orange
# 1,2,3,4,5....
           #1       #2        #3
fruits=["apple", "banana", "orange"]
#           0       1          2


y= len(fruits) # len is the same as length. The length of fruits











                #1          2           3
vegetables = ["cucumber", "eggplant", "bell pepper"] # vegetables becomes ["cucumber", "eggplant", "bell pepper", "mushroom"]

c = len(vegetables)

print(vegetables[0]) # list starts at 0 when accesing elements but starts at 1 when finding the length


vegetables.append("mushroom") # append just means add to the end
print(vegetables)

vegetables.insert(2,"carrot")
print(vegetables)


vegetables.remove("eggplant")
print(vegetables)


vegetables.append("eggplant")
print(vegetables)
vegetables.append("eggplant")
print(vegetables)
vegetables.remove("eggplant")
print(vegetables)
c = vegetables.pop()
print(c)
print(vegetables)
b = vegetables.pop(2)
print(b)
print(vegetables)

vegetables.append("mushroom")
g = vegetables.count("mushroom")
print(vegetables)
print(g)