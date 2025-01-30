numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

evenn = [num for num in numbers if num % 2 == 0]
even_numbers = [num % 2 == 0 for num in numbers]

print(f'Numbers: {numbers}')
print(f'Even numbers: {evenn}')
print(f'Even numbers: {even_numbers}')
