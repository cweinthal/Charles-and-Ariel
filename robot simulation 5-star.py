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


def poly_star(points=5, arm=100):  #predefined  n=4, lenght=100
    angle = 360.0/points
    for x in range(0,points):
    #tip
        left(angle)
        forward(arm)

    #center angle
        left(180-angle/2)

        left(angle)
        #left(180-720/star/4)
        forward(arm)


def wobblestar(points=5, arm=100):
    angle = 360.0/points
    print "Angle= %d, Length= %d"   % (angle, arm)
    for x in range(0,points):
        bot_arm = arm + randint(arm/-10,arm/10)   # length plus an error of +/- 10%
        bot_angle = ((angle // 10) * 10) + 10*randint(-1,1)

    #tip
        left(bot_angle)
        forward(bot_arm)

    #center angle
        left(180-bot_angle/2)
        left(bot_angle)
        #left(180-720/star/4)
        forward(bot_arm)
        print "Bot_Angle= %d  Bot_Arm= %d"  % (bot_angle, bot_arm)



setworldcoordinates(-300,-300,300,300)


home()
pensize(10)
forward(1)   # make a dot

home()
pensize(1)  #reset pen size


home()
color('black')
#poly_star()

home()
color('red')
poly_star(5, 100)

home()
color('blue')
wobblestar(5,100)
color('black')

exitonclick()

wait_for_user()