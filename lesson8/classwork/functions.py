print("My name is Max")

#funtion that returns a greeting massege
def make_greating():
    greeting="hello, world"
    return greeting

messsege=make_greating() # call the make_greeting() function
print(messsege)

# function that builds a face
def build_face():
    return ":)"

face=build_face() # call the build_face() function
print(face)

#functions dont have to return anything
def print_poem():
    print("if i wwere a king,")
    print("i could do anything.")

#you can call functions as many times as you want
print_poem()
print_poem()

#parameters are local variables that can only be accesed inside the funtion:
def personalized_greeting(name): #name is the paramether
    return "hello", name, "!"

personalized_messege=personalized_greeting("alice")
print(personalized_messege)

#funtions that returns a rectangles area based on length and width
def rectangle_area(length,width):#length and width are parameters
    area = length * width
    return area

# when you call a function in a print statement, python will print the funtion returns.
print("the area of a 5x3 rectangle is:", rectangle_area(5,3))