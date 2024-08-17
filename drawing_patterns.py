"""
Samuel Awud
02/22/2023
HW6 - Drawing

"""


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 800

import math
from Gui import *


# Function to draw a line grid with the given parameters
def line_grid(x,y,w,n,c):
    # Calculate the space between each line
    s=math.floor(w/(n-1))
    # Draw each line using the given color and space
    for i in range(n):
        
        canvas.line([[x,y], [x+w,y]], fill=c)
         # Adjust the y-coordinate for the next line.
        y=y-s 


# Function to draw a fan with the given parameters
def fan(x,y,w,n,c,f):
    # Calculate the space between each line
    s=w/(n-1)
    # Calculate the initial x-coordinate for the first line.
    z=x-(w/2)
    if f==True:
        for i in range(n):
            canvas.line([[x,y], [z,y+(w/2)]], fill=c)
            z=z+s 
    # If the fan is facing down, draw each line with a decreasing x-coordinate.
    else:
         for i in range(n):
            canvas.line([[x,y], [z,y-(w/2)]], fill=c)
            z=z+s

# Function to draw alternating fans with the given parameters.

def alternating_fans(x,y,w,nl,nf,c):
    # Calculate the space between each line.
    s=w/(nl-1) 
    for n in range(1,nf+1):
        # If the fan number is odd, draw a fan facing up.
        if n%2==1:
            z=x-(w/2)
            for i in range(nl): 
                canvas.line([[x,y], [z,y+(w/2)]], fill=c)
                z=z+s
            x=x+w
        # If the fan number is even, draw a fan facing down.
        else:
            z=x-(w/2)
            for i in range(nl): 
                canvas.line([[x,y+(w/2)], [z,y]], fill=c)
                z=z+s
            x=x+w

        
# Main function to draw all the line grids and fans.
def main():
    line_grid(-200,300,120,20,"brown")
    line_grid(135,200,200,5,"purple")
    line_grid(-300,-280,90,8,"red")
    fan(0,0,120,10,"blue",True)
    fan(-350,0,200,9,"orange",False)
    fan(200,-200,150,5,"green",False)
    alternating_fans(-350,310,140,15,5,"red")
    alternating_fans(-400,-165,100,4,8,"purple")


# Create a GUI window with a canvas for drawing.
g = Gui()
g.title('HW6 Lines')

# canvas is the drawing area
canvas = g.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
main()
g.mainloop()

'''
To begin, I carefully read the instructions for the homework assignment
 and reviewed the code that was provided. After gaining a thorough 
 understanding of the provided code, I made some modifications to the 
 function parameters so that they would meet the required specifications. 
I then tested the program by running it and observing the output on the
 canvas. The program meets the homework specification by drawing line 
 grids, fans, and alternating fans of different sizes and colors. 
 I learned how to draw different shapes on a canvas using Python, 
 which was an interesting experience. On the next project, I would  
 consider breaking down the code into smaller functions to make it more 
 modular and easier to understand. 
'''














