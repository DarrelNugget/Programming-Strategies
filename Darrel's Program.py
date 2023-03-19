models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Welcome to Circle Phones Profit' calculator. You can calculate your profits for a specific day,\nby week or you can divide the week into weekdays and the weekend.")
print("Welcome to Circle Phones Profit Calculator\n")
startingDay = 0
endingDay = 0

while True:
    sum = 0
    runs = 0
    print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    daySelection = int(input("Enter:\n1 - For specific Day\n2 - For the Week\n3 - For Week Business Days\n4 - For Weekend days\n0 - Exit\n"))
    
    if daySelection == 0:
        break
    elif daySelection == 1: #Single Day
        specificDay = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n")
        if specificDay == "Monday":
            startingDay = 0
            endingDay = 1
    elif daySelection == 2: #Whole Week
        startingDay = 0
        endingDay = 7
    elif daySelection == 3: #Business Days
        startingDay = 0
        endingDay = 5
    elif daySelection == 4: #Weekends
        startingDay = 5
        endingDay = 7    
    else: #this needs to be fix =======================================
        print("invalid input, please enter a valid number\n")
    
    for i in days[startingDay:endingDay]:
        print(f"For {i}")
        runs += 1
        while True:
            
            productCategory = int(input('Enter product number 1-5, or enter 0 to stop:\n'))

            if 0 <= productCategory < 6:
                if productCategory == 0:
                        break
                quantity = int(input('Enter quantity sold:\n'))
                if productCategory == 1:
                    sum += (models['apple phone']*quantity)
                elif productCategory == 2:
                    sum += (models['android phone']*quantity)
                elif productCategory == 3:
                    sum += (models['apple tablet']*quantity)
                elif productCategory == 4:
                    sum += (models['android tablet']*quantity)
                elif productCategory == 5:
                    sum += (models['windows tablet']*quantity)
            else:
                print('Invalid input, please enter a valid number')

        if runs == endingDay:
            if sum >= 10000:
                goodMsg = "You did well this period! Keep up the great work!\n"
                print(f"Your total profit for {i} is: {sum:.2f}\n" + goodMsg)
            elif sum < 10000:
                badMsg = "We didn't reach our goal for this period. More work is needed!\n"
                print(f"Your total profit for {i} is: {sum:.2f}\n" + badMsg)