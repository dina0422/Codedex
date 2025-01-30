#Parameters and Arguments
#Parameters are variables that a fnction takes in as input
#They go inside the parantheses in the function definition and used in the function

#An argument is the value sent to the function when the fx is called

def distance_to_miles(km):
    miles = km / 1.609
    
    print(f'{km} kilometers is {miles} miles')
    
distance_to_miles(1000)
