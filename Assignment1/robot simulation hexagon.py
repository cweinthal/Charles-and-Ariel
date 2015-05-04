#
# Written By CP Weinthal -- perry@weinthal.org ... cweinthal2104@fau.edu
#  Dr. Shankar's Introduction Robotics  COT5930 
# Assignment #1
#
#  Create a Hexagon size 80units per side 
#  Emulate a robot performing the same
#  Then calculate the error between the two
#


from turtle import *
from random import randint
import math

#########################################################
#
#  Polygon
#
#########################################################
def polygon(n=4, length=100):  #predefined  n=4, lenght=100
    angle = 360.0/n
    for i in range(n):
        fd(length)
        lt(angle)

#########################################################
#
#  Robot drawing
#
#########################################################

def wobblegon(n=8, length=80):
    angle = 360.0/n
    total_error = float(0.0)
    error = float(0.0)
    x_error = float(0.0)
    y_error = float(0.0)

    accumaltive_error = float(0.0)
    print "Angle= %d, Length= %d"   % (angle, length)

    for i in range(n):
#Drawing

        bot_length = length + randint(length/-10,length/10)   # length plus an error of +/- 10%
        bot_angle = ((angle // 10) * 10) + 10*randint(-1,1)
        forward(bot_length)
        left(bot_angle)
#Calc errors
        rad_angle = math.radians(angle)
        rad_bot_angle = math.radians(bot_angle)
        err_arm = length-bot_length
        #error = math.fabs(((bot_length * math.tan(rad_bot_angle))/length)*100)
        #error = math.fabs((((length-bot_length) * math.tan(rad_bot_angle))/length)    *100)
        x_error = x_error + (length * math.sin(rad_angle) - bot_length * math.sin(rad_bot_angle))   # x component
        y_error = y_error + (length * math.cos(rad_angle) - bot_length * math.cos(rad_bot_angle))    # y component
        error = math.hypot(x_error, y_error)/length *100

        #accumaltive_error = accumaltive_error + ((length - (bot_length * math.tan(rad_bot_angle)))/length)*1
        #total_error = total_error + error
        print "Bot_Angle= %d  Bot_Len= %d  X_error= %.2f  Y_error= %.2f   Error= %.2f %% "  % (bot_angle, bot_length, x_error, y_error, error)
        #print "Bot_Angle= %d  Bot_Len= %d  Error= %.2f pct Accumulative_Error= %.2f pct Actual_Error= %.2f pct "  % (bot_angle, bot_length, error, total_error, accumaltive_error)
    print "Drawing Error %.2f %% per the graphics" % (100*distance(0,0)/length)

#########################################################
#
#  Main
#
#########################################################

setworldcoordinates(-200,-100,200,300)
home()
pensize(10)
forward(1)   # make a dot

home()
pensize(1)
color('red')
polygon(6, 80)


color('blue')
wobblegon(6,80)
color('blue')

exitonclick()
