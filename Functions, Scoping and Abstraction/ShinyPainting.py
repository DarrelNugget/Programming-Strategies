# Erwin

#Welcome Message and Rooms Input
print("Welcome to Shiny Paint Company for indoor painting!")
totalRoomsInput = int(input("How many rooms do you want to paint:\n"))

#Variables:
paintCoverage = 350
paintCost = 42

#Functions:
def calculateRectangleArea():
    length = float(input("Enter the length of the room in feet:\n"))
    width = float(input("Enter the width of the room in feet:\n"))
    area = length * width
    return area

def computeRectangleWallsAreas():
    length = float(input("Enter the length of the room in feet:\n"))
    width = float(input("Enter the width of the room in feet:\n"))
    height = float(input("Enter the height of the room in feet:\n"))
    area = 2 * ((length * width) + (length * height) + (width * height)) - (2 * (length* width))
    return area

def computeSquareArea():
    length = float(input("Enter the length of one side of the room in feet:\n"))
    area = length ** 2
    return area

def computeSquareWallAreas():
    area = 4 * computeSquareArea()
    return area

def computeWindowsDoorsArea():
    windowsOrDoorsInput = int(input("How many windows and doors the room contain?\n"))
    times = 0
    area = 0
    while times != windowsOrDoorsInput:
        times += 1
        length = float(input(f"Enter windows/door length for window/door {times}\n"))
        width = float(input(f"Enter window/door width for window/door {times}\n"))
        area += length * width
        newArea = area
    return newArea

def computeCustomWallsArea():
    wallAmount = int(input("How many walls are there in the room:\n"))
    times = 0
    area = 0
    while times != wallAmount:
        times += 1
        height = float(input(f"Enter the height of wall {times}\n"))
        length = float(input(f"Enter the length of wall {times}\n"))
        area += height * length
        newArea = area
    return newArea

def computeGallons(area):
    gallons = area / paintCoverage
    return gallons

def computePaintPrice(area):
    paintPrice = computeGallons(area) * paintCost
    return paintPrice

def computeRoomArea():
    totalRooms = totalRoomsInput
    print("Thank you!")
    times = 0
    newArea = 0
    gallons = 0
    paintPrice = 0
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
        gallons += computeGallons(area)
        paintPrice += computePaintPrice(area)
        print(f"For {currentRoom}, " + f"the area to be painted is {area:.1f} square ft and will require {gallons:.2f} gallons to paint. This will cost the customer ${paintPrice:.2f}.")
    return print(f"Area to be painted is {newArea:.1f} square ft and will require {gallons:.2f} gallons to paint. This will cost the customer ${paintPrice:.2f}.")

computeRoomArea()