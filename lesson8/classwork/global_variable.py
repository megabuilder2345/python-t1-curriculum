pet="cat"

def show_pet():
    print("the pet is",pet)

show_pet()

#error: changig a global variabel wwheout declaring global
#ef adopt_dog():
 #  print("the old pet is", pet)
  # pet="dog"
#dopt_dog()
#how_pet()

def adopt_parrot():
    global pet
    pet = "parrot"

adopt_parrot()
show_pet()