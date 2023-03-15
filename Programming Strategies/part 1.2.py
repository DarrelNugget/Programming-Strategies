models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}
sum = 0
while True:

    category = int(input('Enter product number 1-5, or enter 0 to stop:\n '))

    if category > 5:
        print('Invalid input, please enter a valid number')
    else:
        quantity = int(input('Enter quantity sold:\n    '))
        if category == 1:
            sum += (models['apple phone']*quantity)
        elif category == 2:
            sum += (models['android phone']*quantity)
        elif category == 3:
            sum += (models['apple tablet']*quantity)
        elif category == 4:
            sum += (models['android tablet']*quantity)
        elif category == 5:
            sum += (models['windows tablet']*quantity)
        elif category == 0:
            sum = sum
            print('your total profit today is:',sum)
            break