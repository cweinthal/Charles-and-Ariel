#
# Written By CP Weinthal -- perry@weinthal.org ... cweinthal2104@fau.edu
#  Dr. Shankar's Introduction Robotics  COT5930   
# Assignment #1-Extra Credit
#
#  Create a Star 80units per side 
#  Emulate a robot performing the same
#  

from turtle import *
from random import randint

import math


def dot():
    pensize(10)  #pen size to maximum
    forward(0)   # make a dot
    pensize(1)   #reset pen size


def poly_star(points=5, arm=100):  #predefined  n=4, lenght=100
    angle = 180-((180 * (points-2))/points) #calculate the interior angle ... then divide by point

    print "Angle= %d, Length= %d"   % (angle, arm)
    for x in range(0,points):
    #tip
        aangle = angle/2-90
        forward(arm)
        left(aangle)

#        print "Angle_tip= %d, Length= %d"   % (aangle, arm)

    #center angle
        aangle = aangle-180
        forward(arm)
        left(aangle)

#        print "Angle_Center= %d, Length= %d"   % (aangle, arm)
    dot()  #place end dot

def wobblestar(points=5, arm=100):
    angle = 180-((180 * (points-2))/points) #calculate the interior angle ... then divide by point
    print "Angle= %d, Length= %d"   % (angle, arm)
    for x in range(0,points):
        bot_arm = arm + randint(arm/-10,arm/10)   # length plus an error of +/- 10%

    #tip
        bot_angle = ((angle // 10) * 10) + 10* (randint(-1,1))
        aangle = (bot_angle/2)-90

        forward(bot_arm)
        left(aangle)

    #center angle
        bot_arm = arm + randint(arm/-10,arm/10)   # length plus an error of +/- 10%
        bot_angle = ((angle // 10) * 10) + 10* (randint(-1,1))
        aangle = ((bot_angle/2)-90)-180

        forward(bot_arm)
        left(aangle)

    dot()  #place end dot
    # return to origin
    up()
    home()
    down()


################################################################
#
#  Main
#
################################################################
setworldcoordinates(-300,-300,500,500)

home()
dot()

star_points= 5
home()
color('black')

home()
color('red')
poly_star(star_points, 100)

home()
color('blue')
wobblestar(star_points,100)

color('green')
star_points= 9
wobblestar(star_points,100)

exitonclick()
