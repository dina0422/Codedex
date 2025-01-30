#Object is an "instance" of class, 

class Restaurant:
    name = ""
    category = ""
    rating = 0
    delivery = False
    
bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.5
bobs_burgers.delivery = False


#built-in function vars() returns the __dict__ attribute of an object
print(vars(bobs_burgers))

dyno_bites = Restaurant()
dyno_bites.name = 'Dyno Bites'
dyno_bites.category = 'Fast Food'
dyno_bites.rating = 3.5
dyno_bites.delivery = True

print(vars(dyno_bites))