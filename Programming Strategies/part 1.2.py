models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}

sum = 0
while True:

    category = int(input('Enter product number 1-5, or enter 0 to stop:\n    '))

    if category > 5:
        print('Invalid input, please enter a valid number')

    elif category == 1:
        quantity1 = int(input('Enter quantity sold:\n    '))
        sum += (models['apple phone']*quantity1)

    elif category == 2:
        quantity2 = int(input('Enter quantity sold:\n    '))
        sum += (models['android phone']*quantity2)

    elif category == 3:
        quantity3 = int(input('Enter quantity sold:\n    '))
        sum += (models['apple tablet']*quantity3)

    elif category == 4:
        quantity4 = int(input('Enter quantity sold:\n    '))
        sum += (models['android tablet']*quantity4)

    elif category == 5:
        quantity5 = int(input('Enter quantity sold:\n    '))
        sum += (models['windows tablet']*quantity5)

    if category == 0:
        sum = sum
        print('your total profit today is:',sum)
        break