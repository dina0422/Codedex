import csv

data_to_write = [
    ['Name', 'Age', 'Grade'],
    ['Alice', 24, 'A'],
    ['Bob', 19, 'B'],
    ['Charlie', 22, 'C']
]

with open('Intermediate Python/File Input Output/09. Bestsellers/output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file) #create csv write object
    
    csv_writer.writerows(data_to_write) #write data to file
    