# coding=utf-8
"""
COT5930 Assignment 5 the Final - Trianglation- -01 - Due 4/15/15
COT5930  Dr. Shankar
by Huajin Ariel Qu &  Charles Weinthal
Triangulation algorithm for distance esimation - strategy using four Rasp Pis and a server.
"""

from Tkinter import *

#from converters import *

from turtle import *
from Tkinter import Tk, Canvas, Frame, BOTH
from random import  seed, randint
import math
#/sqrt(-b^2+(2*a+200)*b-a^2+200*a-10000)-20/20
def locator(r1,a1,r2,a2,r3,a3,r4,a4):

# camera location defines
    cax = -1
    cay = -1
    cbx = -1
    cby = 9
    ccx = 9
    ccy = 9
    cdx = 9
    cdy = -1
    on = 1
    anglec = 0 +45
    print "r1= %.2f  a1= %.2f  r2= %.2f  a2= %.2f  r3= %.2f  a3= %.2f  r4= %.2f  a4= %.2f  "  % (r1, a1, r2, a2, r3, a3, r4, a4)
    a1 = math.radians(anglec+a1)
    x1= on* cax + (r1 * math.sin(a1)) # ycomponent
    y1= on* cay + (r1 * math.cos(a1))  #y component
#    x1=  (r1 * math.sin(a1)) # ycomponent
#    y1=  (r1 * math.cos(a1))  #y component
    a2 = math.radians(anglec+a2)
    x2= on* cbx + (r2 * math.sin(a2)) # ycomponent
    y2= on* cby - (r2 * math.cos(a2))  #y component
    a3 = math.radians(anglec+a3)
    x3= on* ccx - (r3 * math.sin(a3)) # ycomponent
    y3= on* ccy - (r3 * math.cos(a3))  #y component
    a4 = math.radians(anglec+a4)
    x4= on* cdx - (r4 * math.sin(a4)) # ycomponent
    y4= on* cdy + (r4 * math.cos(a4))  #y component
    print "  x1= %.2f  y1= %.2f x2= %.2f  y2= %.2f x3= %.2f  y3= %.2f   x4= %.2f  y4= %.2f \n"  % (x1, y1, x2, y2, x3,y3, x4,y4)

def hypolocator(r1,r2,r3,r4):
    a = r1**2
    b = r2**2
    c = r3**2
    d = r4**2

#/*   math.sqrt math.sqrt
    print "a= %.2f b= %.2f c= %.2f  d= %.2f  "  % (r1, r2, r3, r4)

#/AB:
#/[x=-(sqrt(-b^2+(2*a+200)*b-a^2+200*a-10000)+20)/20,y=-b-a-80/20],[x=sqrt(-b^2+(2*a+200)*b-a^2+200*a-10000)-20/20,y=-b-a-80/20]]

#    x1a= (math.sqrt((2*a+200)*b-(b**2)-(a**2)+200*a-10000)+20)/20
#   # temp=
#    #x1a=(math.sqrt(b^2+(2*a+200)))  #*b-a^2+200*a-10000)+20)/20
#    y1a= (0-b-a-80)/20
#    x1b= math.sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)-20/20
#    y1b= (0-b-a-80)/20
#    print "  x1a= %.2f  y1a= %.2f x1b= %.2f  y1b= %.2f"  % (x1a, y1a, x1b, y1b)
#/BC:#
#/[[x=-b-a-80/20,y=-sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)-180/20],[x=-b-a-80/20,y=(sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)+180)/20]]
    #x2b= (0-c-b-80)/20
#    y2b= 0-math.sqrt(-c**2+(2*b+200)*c-b**2+200*b-10000)-180/20
#    x2c= (0-c-b-80)/20
#    y2c= (math.sqrt(-c**2+(2*b+200)*c-b**2+200*b-10000)-180)/20
#    print "  x2b= %.2f  y2b= %.2f x2c= %.2f  y2c= %.2f"  % (x2b, y2b, x2c, y2c)


# CD:
# [[x=-sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)-180/20
# y=(b-a+80)/20]
# [x=(sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)+180)/20
# y=(b-a+80)/20]]
# CD:
# [[x=−sqrt(−b^2+(2*a+200)*b−a^2+200*a−10000)−180/20
# #,y=(b−a+80)/20],
# [x=(sqrt(-b^2+(2*a+200)*b−a^2+200*a−10000)+180)/20,
# y=(b−a+80)/20]]

    x3c= 0-math.sqrt(-d**2+(2*c+200)*d-c**2+200*c-10000)+180/20
    y3c= (d-c+80)/20
    x3d= -1*(math.sqrt(-d**2+(2*c+200)*d-c**2+200*c-10000)-180)/20
    y3d= (d-c+80)/20
    print "  x3c= %.2f  y3c= %.2f x3d= %.2f  y3d= %.2f"  % (x3c, y3c, x3d, y3d)

#/DA:
#/ [[x=(b-a+80)/20,y=-(sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)+20)/20],[x=(b-a+80)/20,y=sqrt(-b**2+(2*a+200)*b-a**2+200*a-10000)-20/20]]
#    x4d= (a-b+80)/20
#    y4d= 0-(math.sqrt(-a**2+(2*b+200)*a-b**2+200*b-10000)+20)/20
#    x4a= (a-b+80)/20
#    y4a= math.sqrt(-a**2+(2*b+200)*a-b**2+200*b-10000)-20/20
#    print "  x4d= %.2f  y4d= %.2f x4a= %.2f  y4a= %.2f \n\n"  % (x4d, y4d, x4a, y4a)

    #===================================
locator(7.2111025509,11.309932474,8.4852813742,0,7.2111025509,-11.09932474,5.6568542495,0)  #5,3
hypolocator(7.2111025509, 8.4852813742, 7.2111025509, 5.6568542495)
hypolocator(0,0, 7.2111025509, 8.4852813742)

print "\n\n 3,7"
locator(8.94427191,-18.4349488229,4.472135955,18.4349488229,6.3245553203,26.5650511771,10,-8.1301023542)  #3,7
hypolocator(0,0, 8.94427191, 4.472135955)
hypolocator(0,0, 6.3245553203, 4.472135955)
hypolocator(0,0, 6.3245553203, 10)



"""

############# results

r1= 7.21  a1= 11.31  r2= 8.49  a2= 0.00  r3= 7.21  a3= -11.31  r4= 5.66  a4= 0.00
  x1= 5.00  y1= 3.00 x2= 5.00  y2= 3.00 x3= 5.00  y3= 3.00   x4= 5.00  y4= 3.00

#x ==> y
  x1a= 7.00  y1a= -10.20 x1b= 119.00  y1b= -10.20
  x2b= -10.20  y2b= -129.00 x2c= -10.20  y2c= 15.00
  x3c= -89.00  y3c= 3.00 x3d= 13.00  y3d= 3.00
  x4d= 3.00  y4d= -7.00 x4a= 3.00  y4a= 119.00


r1= 8.94  a1= -18.43  r2= 4.47  a2= 18.43  r3= 6.32  a3= 26.57  r4= 10.00  a4= -8.13
  x1= 3.00  y1= 7.00 x2= 3.00  y2= 7.00 x3= 3.00  y3= 7.00   x4= 3.00  y4= 7.00

#x ==> y
  x1a= 5.00  y1a= -9.00 x1b= 79.00  y1b= -9.00
  x2b= -7.00  y2b= -49.00 x2c= -7.00  y2c= 11.00
  x3c= -129.00  y3c= 7.00 x3d= 15.00  y3d= 7.00
  x4d= 7.00  y4d= -5.00 x4a= 7.00  y4a= 79.00

"""

