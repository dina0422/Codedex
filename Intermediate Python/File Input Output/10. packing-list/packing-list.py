import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    open_file = 'Intermediate Python/File Input Output/10. packing-list/packing-list.csv'
    with open(open_file, 'r') as open_file:
        csv_reader = csv.reader(open_file)
        
        for row in csv_reader:
            print(row)
            
except FileNotFoundError:
    print('Packing list not found. Creating a new one.')
    
    create_file = 'Intermediate Python/File Input Output/10. packing-list/packing-list.csv'
    
    with open(create_file, 'w') as file:
        csv_write = csv.writer(file)
        
        csv_write.writerows(data)