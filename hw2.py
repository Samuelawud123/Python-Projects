# Author Samuel Awud
# Jan 18, 2023
# Two and half hour to finish the program
# Description: Program to calculate and display dimensions 
# and costs for a rectangualr room


import math

# Input section 

print("Welcome to our Interior Design assistant: ")

print(" This program accept the length, width, height of a room and \
the price of one-gallon can of paint and the price per square foot of \
flooring, and calculates the total area of the walls, ceilings, floor, \
the total volume, total length and the total cost for paint and flooring")

#Get the room dimensions and cost of paint and flooring from the user
length = float(input("Please enter a length of the room in feet. "))
width = float(input("Please enter a width of the room in feet. "))
height = float(input("Please enter a height of the room in feet. "))
paintPrice = float(input("Please enter the price of a gallon of paint. $"))
floorPrice = float(input("Please enter the price of one square foot of \
flooring. $"))

# Calculation section - This section does all of the calculations.

#Total area of the walls
totalWallArea = (2 * (length*height)) + 2* (width * height)
#area of ceiling
ceiling = (length*width)
# window area 
windowArea = totalWallArea * 0.1
# The area on the walls and ceilings without the window area
realWallArea= (totalWallArea - (windowArea)) + ceiling
#total Volume
volume = length*width*height
#the total length along the perimeter for the trim
perimeter = 4*(length+width)
#the total area for the floor
floor = math.ceil(length*width)
#total florring cost
floorCost = floor*floorPrice
#named costant/ area to be covered by one gallon
paintCoverage = 350
#total gallons needed
paintGallons = math.ceil(realWallArea/paintCoverage)
#total cost for paint
paintCost = paintGallons*paintPrice


''' Output section - This section displays the user inputs back, and 
calculated dimensions, and costs.'''


print("From the Dimension and Price you gave us: ")
print("The length of the room is:",length,"ft.")
print("The width of the room is:",width,"ft.")
print("The height of the room is:",height,"ft.")
print("The Price of the paint is: $",paintPrice,)
print("The Price of the floor is: $",floorPrice,)



print("And the Calculated Dimensions and costs are: ")
print("The total area on the walls and ceiling is : ", realWallArea,"sq. ft.")
print("The amount flooring needed is:",floor,"sq. ft.")
print("The total room volume is:",volume, "cu. ft.")
print("The total amount of trim needed is:",perimeter,"ft")
print("The cost of flooring will be: $",floorCost)
print("The room will require",paintGallons,"gallons of paint.")
print("The cost of paint will be: $",paintCost)


''' 
1) I started the program by reading the description and 
by tring to understand the problem clearly. Most of the program 
was easy to understand when I read it at first and I started coding. 
However, I got stuck while  calculating the wall area and it consumed
 majority of the time I spent on this homework. I, finally, solved the
 problem by using the maths I learned in high school.


2) As soon as I finished writing the program, I tested it with different
 numbers including these numbers listed below.
I used      length = 10ft
            Width =12ft
            height=15ft
            paintPrice= $5
            floorPrice= $25
And got these: 
            realWallArea= 714.0 sq. ft.
            floor= 120 sq. ft.
            volume= 1800.0 cu. ft.
            perimeter= 88.0 ft
            floorCost= $3000.0
            paintGallons= 3 gallons
            paintCost=  $15


3)I have learned many things in this program, including how to use the ceiling function,
  and starting from now, I have decided to plan my code on a paper before I start coding, 
  I believe that will the coding much easier.
 '''