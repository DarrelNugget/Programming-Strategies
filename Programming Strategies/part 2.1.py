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

#moved the days_value into while loop below

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


    #if (days > 4):
        #print('invalid input, please enter a valid number')
        #moved this line up 


    if(days == 1):#one day
        day_value+=1

        spec_days = (input('''
    Enter a specific day [Monday, Tuesday, 
    Wednesday, Thursday, Friday, Saturday, 
    Sunday]

    '''))
    elif(days == 2):#whole week
        day_value+=7
    elif(days == 3):#work week
        day_value+=5
    elif(days == 4):#weekends
        day_value+=2

    sum = 0
    for i in range(0,day_value):
        print(f'for {named_days_value.keys()}\n')
        while True:
            #so the for whatever day doesnt repeat, its been moved out of the while loop
            category = int(input('Enter product number 1-5, or enter 0 to stop:\n'))

            if 0 <= category < 6:
                if category == 0:
                    print('your total profit today is:',sum,'\n')
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