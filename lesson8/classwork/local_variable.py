#local variable a variable made inside a funtion, that only exisets inside a funtion
def adopt_dog():
    pet = "dog" # pet is a local variable
    print("the pet is:," pet)

adopt_dog()

#error: trying to use pet outside its funtion
#rint(pet)
