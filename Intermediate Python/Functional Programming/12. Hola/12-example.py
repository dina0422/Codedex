#higher order functions - take functions as arguments or return fx as a results

def apply_operation(operation, numbers):
    result = []
    for num in numbers:
        result.append(operation(num)) #add the result of the operation to the list
    return result

def double(x):
    return x * 2

numbers_list = [1, 2, 3, 4, 5]

#higher order function
doubled_numbers = apply_operation(double, numbers_list)

print(f'Original Numbers: {numbers_list}')
print(f'Doubled Numbers: {doubled_numbers}')