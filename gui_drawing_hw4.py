
# Name:Samuel Hassen
# Date: 02/02/2023
# HW4- practice in GUI and functional decomposiion

from Gui import *

# This function draws a car using rectangles and a circle
# x,y are the coordinates for placement
# 'color' defines object color
#'ratio' adjusts object size


def car (x,y,color,ratio):
    
    canvas.rectangle([[x,y],[x+200*ratio,y+40*ratio]], fill=color)
    canvas.polygon([[x+50*ratio,y+40*ratio],[x+75*ratio,y+80*ratio],[x+125*ratio,y+80*ratio],[x+150*ratio,y+40*ratio]],fill="#E1E1E1")
    canvas.circle([x+35*ratio,y],17*ratio,fill="#E1E1E1",width=5)
    canvas.circle([x+165*ratio,y],17*ratio,fill="#E1E1E1",width=5)
    #canvas.line([[x+100*ratio,y-30*ratio],[x+100*ratio,y+100*ratio]]) # test line

# This function raws a triangular tree using rectangles and triangles
# x,y are the coordinates for placement
# 'color' defines object color
#'ratio' adjusts object size


def tritree(x,y,ratio,color1,color2):
    canvas.rectangle([[x,y],[x+25*ratio,y+100*ratio]], fill=color2)
    canvas.polygon([[x-25*ratio,y+75*ratio],[x+50*ratio,y+75*ratio],[x+12.5*ratio,y+175*ratio]], fill=color1)
    #canvas.line([[x+12.5*ratio,y-25*ratio],[x+12.5*ratio,y+200*ratio]]) # test line

# This function draws an oval tree using rectangles and ovals
# x,y are the coordinates for placement
# 'color' defines object color
#'ratio' adjusts object size




def ovaltree(x,y,ratio,color1,color2):
    canvas.rectangle([[x+25*ratio,y-20],[x+50*ratio,y+100*ratio]], fill=color2)
    canvas.oval([[x,y+75*ratio],[x+75*ratio,y+225*ratio]], fill=color1)
    #canvas.line([[x+37.5*ratio,y-30],[x+37.5*ratio,y+235*ratio]]) # test line


# This function draws a house using rectangles and triangles
# x,y are the coordinates for placement
# 'color' defines object color
#'ratio' adjusts object size




def house (x,y,color,ratio):
    canvas.rectangle([[x,y],[x+250*ratio,y+150*ratio]], fill=color)
    canvas.polygon([[x-50*ratio,y+150*ratio],[x+300*ratio,y+150*ratio],[x+125*ratio,y+250*ratio]], fill="#8C8A80")    
    canvas.rectangle([[x+25*ratio,y],[x+75*ratio,y+100*ratio]], fill="#39A09C")
    canvas.rectangle([[x+150*ratio,y+50*ratio],[x+187.5*ratio,y+100*ratio]], fill="#39A09C",width=3)
    canvas.rectangle([[x+187.5*ratio,y+50*ratio],[x+225*ratio,y+100*ratio]], fill="#39A09C",width=3)
    #canvas.line([[x+125*ratio,y-25*ratio],[x+125*ratio,y+275*ratio]]) # test line
    
def main():
    car(0,0,"#E9B726",1)
    car(300,-225,"#E9B726",0.75)
    car(-450,0,"#E9B726",0.75)
    car(-50,-275,"#E9B726",0.75)
    tritree(250,-200,1,color1="#5DCF0D",color2="#A6910B")
    tritree(470,-25,1,color1="#5DCF0D",color2="#A6910B")
    tritree(-50,125,0.75,color1="#5DCF0D",color2="#A6910B")
    tritree(120,140,0.5,color1="#5DCF0D",color2="#A6910B")
    ovaltree(-470,-270,1,color1="#5DCF0D",color2="#A6910B")
    ovaltree(400,-25,0.5,color1="#5DCF0D",color2="#A6910B")
    ovaltree(-210,25,1,color1="#5DCF0D",color2="#A6910B")
    ovaltree(50,125,0.75,color1="#5DCF0D",color2="#A6910B")
    house(-480,75,"#9C5700",0.75)
    house(250,0,"#9C5700",0.5)
    house(350,150,"#9C5700",0.5)
    house(-300,-270,"#9C5700",0.75)
    


g=Gui()
g.title("HW4: Drawing")
canvas = g.ca(1040,600)
canvas.rectangle([[-520,-300],[520,300]],fill="#005FD3")


main()
g.mainloop()

"""I began the task by sketching a draft on paper and noting the coordinate
 points. I attempted to duplicate the first house I drew to another set 
of coordinates, but I encountered difficulty moving the window along with
the house. This was due to using separate functions and parameters for 
the window and house. However, I eventually succeeded. Through this 
week's homework, I have gained experience in using GUI functions with
 parameters and applying the concept of functional decomposition."""



