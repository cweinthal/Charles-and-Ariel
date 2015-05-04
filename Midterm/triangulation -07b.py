# coding=utf-8
"""
COT5930 Assignment 5 the Final - Trianglation- -01 - Due 4/15/15
COT5930  Dr. Shankar
by Huajin Ariel Qu &  Charles Weinthal
Triangulation algorithm for distance esimation - strategy using four Rasp Pis and a server.
"""

#from Tkinter import *

#from converters import *

#from turtle import *
#from Tkinter import Tk, Canvas, Frame, BOTH
#from random import  seed, randint
import math
#/sqrt(-b^2+(2*a+200)*b-a^2+200*a-10000)-20/20

# Insert your DISTANCE error code here
def ed(l):
    l= l
    return l

# Insert your ANGLE error code here
def ea(a):
    a= a
    return a

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
    x1= on* cax + (ed(r1) * math.sin(ea(a1))) # ycomponent
    y1= on* cay + (ed(r1) * math.cos(ea(a1)))  #y component
#    x1=  (r1 * math.sin(a1)) # ycomponent
#    y1=  (r1 * math.cos(a1))  #y component
    a2 = math.radians(anglec+a2)
    x2= on* cbx + (ed(r2) * math.sin(ea(a2))) # ycomponent
    y2= on* cby - (ed(r2) * math.cos(ea(a2)))  #y component
    a3 = math.radians(anglec+a3)
    x3= on* ccx - (ed(r3) * math.sin(ea(a3))) # ycomponent
    y3= on* ccy - (ed(r3) * math.cos(ea(a3)))  #y component
    a4 = math.radians(anglec+a4)
    x4= on* cdx - (ed(r4) * math.sin(ea(a4))) # ycomponent
    y4= on* cdy + (ed(r4) * math.cos(ea(a4)))  #y component
# find the best vector
    best_r= min(abs(r1), abs(r2), abs(r3), abs(r4))
    if best_r == r1:
        camera_d = "a"
    elif best_r == r2:
        camera_d = "b"
    elif best_r == r3:
        camera_d = "c"
    else:
        camera_d = "d"
    aa1= (a1*a1)
    aa2= (a2*a2)
    aa3= a3*a3
    aa4= a4*a4

    best_a= min (aa1, aa2, aa3, aa4)
    if best_a == a1:
        camera_a =  "a"
    elif best_a == a2:
        camera_a = "b"
    elif best_a == a3:
        camera_a = "c"
    else:
        camera_a = "d"





    print " Best two cameras: By distance = %s  By Angle = %s \n" % (camera_d, camera_a)

    print "  x1= %.2f  y1= %.2f x2= %.2f  y2= %.2f x3= %.2f  y3= %.2f   x4= %.2f  y4= %.2f \n"  % (x1, y1, x2, y2, x3,y3, x4,y4)

def hypolocator(r3,r4,a,b):

    c = r3**2
    d = r4**2

#/*   math.sqrt math.sqrt
    print " c= %.2f  d= %.2f "  % (r3, r4)
    a= -1*(math.sqrt(-d**2+(2*c+200)*d-c**2+200*c-10000)-180)/20
    b= (d-c+80)/20
    print " Using distance only x= %.2f  y= %.2f"  % (a,b)



    #===================================
a=0
b=0
locator(7.2111025509,11.309932474,8.4852813742,0,7.2111025509,-11.09932474,5.6568542495,0)  #5,3
#hypolocator(7.2111025509, 5.6568542495,a,b)
#hypolocator(7.2111025509, 8.4852813742,a,b)

print "\n\n 3,7"
locator(8.94427191,-18.4349488229,4.472135955,18.4349488229,6.3245553203,26.5650511771,10,-8.1301023542)  #3,7

#hypolocator(6.3245553203, 4.472135955,a,b) #CB
#hypolocator(6.3245553203, 10,a,b) #CD
