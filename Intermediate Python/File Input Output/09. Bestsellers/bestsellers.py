import csv

csv_file_path = 'Intermediate Python/File Input Output/09. Bestsellers/Bestseller - Sheet1.csv'

best_selling_book = None
highest_sales = 0

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    csv_file.readline() #skip the header
    
    for row in csv_reader:
        current_sales = float(row[4])
        
        if current_sales > highest_sales:
            highest_sales = current_sales
            best_selling_book = row
            
output_file_path = 'Intermediate Python/File Input Output/09. Bestsellers/bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])
    
print(f'Bestselling info written to {output_file_path}')
        
        