def get_item(item):
    if item == 1:
        return '🍔 Cheeseburger'
    elif item == 2:
        return '🍟 Fries'
    elif item == 3:
        return '🥤 Soda'
    elif item == 4:
        return '🍦 Ice cream'
    elif item == 5:
        return '🍪 Cookie'
    else:
        return '🚫 Invalid item.'
    
def welcome():
    print('Welcome to the drive-thru!')
    print('May I take your order?')
    print('1. 🍔 Cheeseburger')
    print('2. 🍟 Fries')
    print('3. 🥤 Soda')
    print('4. 🍦 Ice cream')
    print('5. 🍪 Cookie')


welcome()
order = int(input('Enter the number of the item you want: '))
print(get_item(order))
    