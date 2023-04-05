

#Gabes code and what ive got done so far


paint_coverage = 350 #paint coverage for ft2/gal
gallon_cost = 42 #price per #CDN/gal
labor_cost = 0 #included in price of paint

def compute_room_area(room_num, Custom_Wall_Area, rectangle_area, square_area, Windows_Doors_Area, total_area, Paint_Price):
    options = int(input('''
Select the Shape of the Room:
1-Rectangular
2-Square
3-Custom (more or less than 4 walls, all square or rectangles)\n'''))
    

    if options == 1:
        #area of the room 
        #print room number
        #area to be painted
        #cost

        return
    
    





def compute_Rectangle_Walls_Area(options):
    length = int(input('what is the length of the room in feet: \n'))
    width = int(input('what is the width of the room in feet: \n'))
    height = int(input('what is the height of the room in feet: \n'))
    #area = height * (width or length)
    return

def calculate_Rectangle_Area(length, width, height):
    rectangle_area = height * (width or length)
    return rectangle_area

def compute_Square_Walls_Area():
    side_room_length = int(input('Enter the length of one side of the room: \n'))

def compute_Square_Area(side_room_length):
    wall_1 = side_room_length * 2
    square_area = wall_1 * 4
    return square_area

def compute_Windows_Doors_Area():
    windows_doors = int(input('How many windows and doors does the room contain? \n'))
    WD_Length = 0 #WD = Windows, Door
    WD_Width = 0
    for i in windows_doors:
        WD_Length += int(input(f'Enter window/door length for the window/door {i} in feet\n'))
        WD_Width += int(input(f'ENter windoe/door width for window/door {i} in feet\n'))

    Windows_Doors_Area = WD_Length * WD_Width
    return Windows_Doors_Area

def compute_Custom_Walls_Area(windows_doors):
    Custom_Walls_num = int(input('How many walls are there in the room \n'))
    CW_height = 0 #CW = Custom Walls
    CW_length = 0
    for i in Custom_Walls_num:
        CW_height += int(input(f'Enter the height of wall {i} in feet'))
        CW_length += int(input(f'Enter the length of wall {i} in feet'))

    Custom_Wall_Area = CW_height * CW_length
    return Custom_Wall_Area

def compute_Gallons(rectangle_area, square_area, Custom_Wall_Area, Windows_Doors_Area):
    gallon = 0
    total_area = ((square_area + rectangle_area + Custom_Wall_Area) - Windows_Doors_Area)
    gallon += total_area / paint_coverage
    return gallon

def compute_Paint_Pice(gallon):
    Paint_Price = gallon * gallon_cost
    return Paint_Price



print('Welcome to Shiny Paint Company for indoor painting!\n')
room_num = int(input('How many rooms do you want to paint: \n'))

for i in room_num:
    print('Room:',i)

#input the methods