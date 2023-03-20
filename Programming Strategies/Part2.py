models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

programRunning = True

print("Welcome to Circle Phones Profit' calculator. You can calculate your profits for a specific day,\nby week or you can divide the week into weekdays and the weekend.")
print("Welcome to Circle Phones Profit Calculator\n")

while programRunning == True:
    sum = 0
    startingDay = 0
    endingDay = 0
    print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    #Loop to determine profit of specific days or weeks or weekends..... etc
    while True:
        daySelection = int(input("Enter:\n1 - For specific Day\n2 - For the Week\n3 - For Week Business Days\n4 - For Weekend days\n0 - Exit\n"))
        #Picking one will set the range of the list 
        if daySelection == 0:
            programRunning = False
            break
        elif daySelection == 1: #Single Day
            specificDay= input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n")
            upperCheck = specificDay.upper()
            if upperCheck == "MONDAY":
                startingDay = 0
                endingDay = 1
            elif upperCheck == "TUESDAY":
                startingDay = 1
                endingDay = 2
            elif upperCheck == "WEDNESDAY":
                startingDay = 2
                endingDay = 3
            elif upperCheck == "THURSDAY":
                startingDay = 3
                endingDay = 4
            elif upperCheck == "FRIDAY":
                startingDay = 4
                endingDay = 5
            elif upperCheck == "SATURDAY":
                startingDay = 5
                endingDay = 6
            elif upperCheck == "SUNDAY":
                startingDay = 6
                endingDay = 7
            break
        elif daySelection == 2: #Whole Week
            startingDay = 0
            endingDay = 7
            break
        elif daySelection == 3: #Business Days
            startingDay = 0
            endingDay = 5
            break
        elif daySelection == 4: #Weekends
            startingDay = 5
            endingDay = 7
            break
        else:
            print("invalid input, please enter a valid number\n")

    #Set the message for profit depending on the daySelection
    if daySelection == 1:
        profitMessage = specificDay.lower()
        profitMessage = specificDay.capitalize()
    elif daySelection == 2:
        profitMessage = "week"
    elif daySelection == 3:
        profitMessage = "week (business days)"
    elif daySelection == 4:
        profitMessage = "weekend"

    #Loop to calc the profit total
    for i in days[startingDay:endingDay]:
        print(f"For {i}")
        while True:
            
            productCategory = int(input('Enter product number 1-5, or enter 0 to stop:\n'))
            #Calc the sum depending on the model picked and amount sold
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
        #Determines if the sum is greater or less than 10000
        if (days.index(i) + 1) == endingDay:
            if sum >= 10000:
                goodMsg = (f"You did well this {profitMessage}! Keep up the great work!\n")
                print(f"Your total profit for the {profitMessage} is: ${sum:.2f}\n" + goodMsg)
            elif sum < 10000:
                badMsg = (f"We didn't reach our goal for this {profitMessage}. More work is needed!\n")
                print(f"Your total profit for the {profitMessage} is: ${sum:.2f}\n" + badMsg)

print("Program End!")