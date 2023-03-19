models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}

named_days_value = {
    'Monday':0,
    'Tuesday':0,
    'Wednesday':0,
    'Thursday':0,
    'Friday':0,
    'Saturday':0,
    'Sunday':0,
}

print('Welcome to Circle Phones Profit calculator\n')
#looped the welcome

day_value = 0

while True:

    print('You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend')
    days = int(input('''
    Enter:
    1-For a specific day
    2-For the week
    3-For the week buisness days
    4-For weekend days
    0-Exit

    '''))

    if(days == 0):#stop the program
        break
    elif (days > 4):
        print('invalid input, please enter a valid number')


    if(days == 1):#this should be working now
        day_value+=1
        spec_days = (input('''
    Enter a specific day [Monday, Tuesday, 
    Wednesday, Thursday, Friday, Saturday, 
    Sunday]

    '''))
        first = spec_days[0]
        rest = spec_days[1:]
        for keys in named_days_value:
            day = first.upper() + rest.lower()
            if day == keys:
                print("For",keys)

    elif(days == 2):#whole week
        day_value+=7
        
    elif(days == 3):#work week
        day_value+=5
    elif(days == 4):#weekends
        day_value+=2

    sum = 0
    for i in range(0,day_value):
        #for statement might not be needed
        while True:
            if days == 2:
                for week in named_days_value.keys[keys]:
                    print(f'for {week}')
                
            category = int(input('Enter product number 1-5, or enter 0 to stop:\n'))

            if 0 <= category < 6:
             #added message for high sums
                if category == 0 and sum >= 10000:
                    goodMsg = "You did well this period! Keep up the great work!"
                    print(f'Your total profit for {day} is: {sum:.2f} ' + goodMsg)
                    break
                #added message for low sums
                if category == 0 and sum < 10000:
                    badMsg = "We didn't reach our goal for this period. More work is needed!"
                    print(f'Your total profit for {day} is: {sum:.2f} ' + badMsg)
                    break
                    

                quantity = int(input('Enter quantity sold:\n'))

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
            else:
                print('Invalid input, please enter a valid number')
    if days == i:
        break