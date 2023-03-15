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
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['apple phone']*quantity)

    elif category == 2:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['android phone']*quantity)

    elif category == 3:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['apple tablet']*quantity)

    elif category == 4:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['android tablet']*quantity)

    elif category == 5:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['windows tablet']*quantity)

    if category == 0:
        sum = sum
        print('your total profit today is:',sum)
        break