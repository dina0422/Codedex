import random
from functools import reduce 

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

#mapped names
def capitalize_suffix(name):
    return name.capitalize()

capital_suffix = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

#list comprehension
random_name = [
    create_fantasy_name(prefixes, capital_suffix) 
    for name in range(10)
    ]

#filtered names
def fire_in_name(name):
    return 'Fire' in name

filtered_names = list(filter(fire_in_name, random_name))

#reduced list based on the filtered names
def concatenate_names(name1, name2):
    return name1 + ', ' + name2

reduced_names = reduce(concatenate_names, filtered_names)

def display_name_info():
    print("Fantasy names:")
    for name in random_name:
        print(name)
    print(f'Filtered names with \'Fire\': {filtered_names}')
    print(f'Concatenated names: {reduced_names}')
    
display_name_info()


    