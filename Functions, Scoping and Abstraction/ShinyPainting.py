#Messages and Rooms Input
print("Welcome to Shiny Paint Company for indoor painting!")
totalRoomsInput = int(input("How many rooms do you want to paint:\n"))
print("Thank you!")

#Variables:
paintCoverage = 350
paintCost = 42

#Functions:
def computeRoomArea():
    totalRooms = totalRoomsInput
    #New variables for this function
    times = 0
    newArea = 0
    newGallons = 0
    newPaintPrice = 0
    while times != totalRooms:
        times += 1
        currentRoom = f"Room: {times}"
        print(currentRoom)
        roomShape = int(input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls , all square or rectangles)\n"))
        if roomShape == 1:
            area = computeRectangleWallsAreas() - computeWindowsDoorsArea()
        if roomShape == 2:
            area = computeSquareWallAreas() - computeWindowsDoorsArea()
        if roomShape == 3:
            area = computeCustomWallsArea() - computeWindowsDoorsArea()
        newArea += area
        gallons = computeGallons(area)
        paintPrice = computePaintPrice(area)
        newGallons += gallons
        newPaintPrice += paintPrice
        print(f"For {currentRoom}, " + f"the area to be painted is {area:.1f} square ft and will require {gallons:.2f} gallons to paint. This will cost the customer ${paintPrice:.2f}.")
    return print(f"Area to be painted is {newArea:.1f} square ft and will require {newGallons:.2f} gallons to paint. This will cost the customer ${newPaintPrice:.2f}.")

#Total Surface Area of Walls in Rectangular Room
def computeRectangleWallsAreas():
    length = float(input("Enter the length of the room in feet:\n"))
    width = float(input("Enter the width of the room in feet:\n"))
    height = float(input("Enter the height of the room in feet:\n"))
    rectangleWallsAreas = 2 * ((length * width) + (length * height) + (width * height)) - (2 * calculateRectangleArea(length, width))
    return rectangleWallsAreas

#Calculate rectangle area
def calculateRectangleArea(length, width):
    rectangleArea = length * width
    return rectangleArea

#Total Surface Area of Walls in Square Room
def computeSquareWallAreas():
    length = float(input("Enter the length of one side of the room in feet:\n"))
    squareWallAreas = 4 * computeSquareArea(length)
    return squareWallAreas

#Calculate square area
def computeSquareArea(length):
    squareArea = length ** 2
    return squareArea

#Sum of all windows/doors in room
def computeWindowsDoorsArea():
    windowsOrDoorsInput = int(input("How many windows and doors the room contain?\n"))
    times = 0
    windowsDoorsArea = 0
    while times != windowsOrDoorsInput:
        times += 1
        length = float(input(f"Enter windows/door length for window/door {times}\n"))
        width = float(input(f"Enter window/door width for window/door {times}\n"))
        windowsDoorsArea += length * width
    return windowsDoorsArea

#Total Surface Area of Walls in Custom Room
def computeCustomWallsArea():
    wallAmount = int(input("How many walls are there in the room:\n"))
    times = 0
    customWallsArea = 0
    while times != wallAmount:
        times += 1
        height = float(input(f"Enter the height of wall {times}\n"))
        length = float(input(f"Enter the length of wall {times}\n"))
        customWallsArea += height * length
    return customWallsArea

#Calculate gallons of paint needed
def computeGallons(area):
    gallons = area / paintCoverage
    return gallons

#Price of paint needed
def computePaintPrice(area):
    paintPrice = computeGallons(area) * paintCost
    return paintPrice

#Starts function
computeRoomArea()