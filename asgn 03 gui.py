__author__ = 'ofuzzy1'
#from Tkinter import *
#from converters import *
from turtle import *
from Tkinter import Tk, Canvas, Frame, BOTH

from random import  seed, randint
import math
import numpy as np
import matplotlib.pyplot as plt

angles=[]  # position 0 is the demo value
chords=[]  # position 0 is the demo value
n = 4
r_angles=[]
r_chords=[]
e_position=[]
seed(2)


def gohome():
    penup()
    home()
    pendown()

def dot():
    pensize(10)
    forward(0)   # make a dot
    pensize(1)

def polygon(n=4, length=100):  #predefined  n=4, length=100
#        global angle
#        global length
#        global n
    angle = 360.0/n
    global r_angles
    global r_chords
    for i in range(n):
        lt(angle)
        fd(length)
        r_length = length   # length plus an error of +/- 10%
        r_angle = angle
        r_angles.append(r_angle)
        r_chords.append(r_length)
        if xcor() > -50:
           algn="left"
           text = "______" + str(position())
        else:
            algn="right"
            text = str(position()) + "______"
        write(text, align=algn)



def wobblegon(n=8, length=80):
    global angles
    global chords
    #global bot_angle
#    global n
    angle = 360.0/n
#    angles.append(angle)
#    chords.append(length)  #position 0 is the ideal value

    for i in range(n):
#Drawing

        bot_length = length + randint(length/-10,length/10)   # length plus an error of +/- 10%
        bot_angle = ((angle // 10) * 10) + 10*randint(-1,1)
        angles.append(bot_angle)
        chords.append(bot_length)
        left(bot_angle)
        forward(bot_length)

        if xcor() > -50:
            algn="left"
            text = "______" + str(position())
        else:
            algn="right"
            text = str(position()) + "______"
        write(text, align=algn)



    angles[0]= angle  #[0] is the reference position
    chords[0]= length

class App:

    def __init__(gui, master):
 #       gui.t_conv = ScaleAndOffsetConverter('C', 'F', 1.8, 32)
        frame = Frame(master)
        frame.pack()
        Label(frame, text='How Many Corners?').grid(row=0, column=0)
        Label(frame, text='3 > # > 20').grid(row=0, column=4)
        gui.ang_var = IntVar()
   #     gui.ang_var = 6

        Entry(frame, textvariable=gui.ang_var).grid(row=0, column=1)

        Label(frame, text='Length of Side?').grid(row=1, column=0)
        Label(frame, text='30 > L > 100').grid(row=1, column=4)
        gui.chord_var = IntVar()
#        gui.chord_var = 80
#        gui.insert(0, 'Type words here')
        Entry(frame, textvariable=gui.chord_var).grid(row=1, column=1)

#        Label(frame, textvariable=gui.result_var).grid(row=3, column=1)
        Label(frame, text='Messages').grid(row=3, column=0)

#        Label(frame, text='deg F').grid(row=1, column=0)
        gui.result_var =  StringVar()  #DoubleVar()
        Label(frame, textvariable=gui.result_var).grid(row=3, column=1)
#        button = Button(frame, text='Draw', command=gui.convert)
        button = Button(frame, text='Draw', command=gui.draw)
        button.grid(row=4,  column=0)
        button = Button(frame, text='Info', command=gui.info)
        button.grid(row=4,  column=1)
        button = Button(frame, text='Error Graph', command=gui.error)
        button.grid(row=4,  column=2)
        button = Button(frame, text='Histogram Plot', command=gui.histogram)
        button.grid(row=4,  column=3)
        button = Button(frame, text='Exit', command=gui.exit)
        button.grid(row=4,  column=4)
    def error(gui):
        if len(angles)==0:
            gui.result_var.set("Please use Draw first.")
        else:
            global length
            global n
            angle = 360/n
            root.title('Robot Demostration GUI')
            w=300
            h=200

            canvas = Canvas(root, width =w, height=h)

    # from http://www.java2s.com/Code/Python/CatalogPython.htm
            # graph the angles
            canvas.create_text(w/4, 10, text='Angle')
            canvas.create_line(0,h-angle,((w/2)-5),h-angle)


            canvas.create_line(((w/2)+5),h-length,(w-5),h-length)
            canvas.create_text(3*w/4, 10, text='Length')

            offset = ((w/2) / n)-5
     #       print (offset)
            for i in range(n-2):
            # graph the angles
                canvas.create_line(offset*i ,h-angles[i],offset*(i+1) ,h-angles[i+1])
            # graph the lengths
                canvas.create_line((w/2)+offset*i +10,h-chords[i],(w/2)+offset*(i+1) +10,h-chords[i+1])

            canvas.pack()



    def convert(gui):
        c = gui.c_var.get()
        gui.result_var.set(gui.t_conv.convert(c))

    def draw(gui):
        seed(2)
        global angle
        global length
        global n

        n = gui.ang_var.get()
        length = gui.chord_var.get()
 #       print n, length
 #       print "N= %d  Len= %d "  % (n, length)

        if n <4 or n> 20:
            gui.result_var.set("#Corners must be larger than 3 and smaller than 21")
            # tkMessageBox.showwarning(
            #     "Wrong Data",
            #     "#Corners must be larger than 3 and smaller than 21"
            # )

        elif length <30 or length >100:
            gui.result_var.set("Length must be larger than 29 and smaller than 100")

        else:
            gui.result_var.set(" Great, let's begin to draw!                      ")

            setworldcoordinates(-1*length*(n/2),-1*length,length*(n/4),length*(2+(n/2)))
            gohome()
            dot()

            pensize(1)
            color('red')
            gohome()
            polygon(n, length)
            penup()

            color('blue')
            gohome()
            wobblegon(n, length)
 #            penup()
 #            home()
 # #           exitonclick()



    def histogram(gui):
        if len(angles)==0:
            gui.result_var.set("Please use Draw first.")
        else:
            global length
            global n
            gui.info(gui)
            fig, ax=plt.subplots(2,2)
            index=np.arange(n)
            bar_width=0.35
            opacity=0.4
            plt.subplot(221)
            rects1 = plt.bar(index, chords, bar_width,alpha=opacity, color='b',label=    'True length')
            rects2 = plt.bar(index + bar_width, r_chords, bar_width,alpha=opacity,color='r',label=   'Ideal length')

            #rects1 = plt.bar(index, r_chords, bar_width,alpha=opacity, color='b',label=   'Ideal length')
            plt.xlabel('Points(Blue-true values, pink-ideal values)')
            plt.ylabel('Length')
            plt.title('Histogram plot of error length')
            #plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
            #plt.ylim(0,100)
            #plt.legend()
            plt.tight_layout()

            plt.subplot(222)
            rects1 = plt.bar(index, angles, bar_width,alpha=opacity, color='b',label=    'True angle')
            rects2 = plt.bar(index + bar_width, r_angles, bar_width,alpha=opacity,color='r',label=   'Ideal angle')

            #rects1 = plt.bar(index, r_chords, bar_width,alpha=opacity, color='b',label=   'Ideal length')
            plt.xlabel('Points(Blue-true values, pink-ideal values)')
            plt.ylabel('Angles')
            plt.title('Histogram plot of error angle')
            #plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
            #plt.ylim(0,100)
            #plt.legend()
            plt.tight_layout()

            plt.subplot(223)
            rects1 = plt.bar(index, e_position, bar_width,alpha=opacity, color='b',label=    'Position Error')
            #rects2 = plt.bar(index + bar_width, r_angles, bar_width,alpha=opacity,color='r',label=   'Ideal angle')

            #rects1 = plt.bar(index, r_chords, bar_width,alpha=opacity, color='b',label=   'Ideal length')
            plt.xlabel('Points')
            plt.ylabel('Position Error')
            plt.title('Histogram plot of error position')
            #plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
            #plt.ylim(0,100)
            #plt.legend()
            plt.tight_layout()
            #position error
            #for i in range(n):
                ##Drawing

                        #bot_length = length + randint(length/-10,length/10)   # length plus an error of +/- 10%
                        #bot_angle = ((angle // 10) * 10) + 10*randint(-1,1)
                ##Calc errors
                # store BOTH old angles for summation

                        #old_bot_angle = old_bot_angle + bot_angle
                        #old_angle = old_angle + angle
                        #rad_angle = math.radians(old_angle)
                        #rad_bot_angle = math.radians(old_bot_angle)
                        #x_error = x_error + (length * math.sin(rad_angle) - bot_length * math.sin(rad_bot_angle))   # x component
                        #y_error = y_error + (length * math.cos(rad_angle) - bot_length * math.cos(rad_bot_angle))    # y component
                        #error = math.hypot(x_error, y_error)/length *100
                        ##quote= "Bot_Angle= %d  Bot_Len= %d \n"  % (bot_angle, bot_length)
                        #e_position.append(error)

            #rects1 = plt.bar(index, e_position, bar_width,alpha=opacity, color='b',label=    'Position Error')
            #rects2 = plt.bar(index + bar_width, r_angles, bar_width,alpha=opacity,color='r',label=   'Ideal angle')

            #rects1 = plt.bar(index, r_chords, bar_width,alpha=opacity, color='b',label=   'Ideal length')
            #plt.xlabel('Points')
            #plt.ylabel('Position')
            #plt.title('Histogram plot of position error')
            ##plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
            ##plt.ylim(0,100)
            #plt.legend()
            #plt.tight_layout()

            plt.show()


    def calc(self):
        c=0


    def exit(gui):
        root.quit()

    def info(gui):
        global e_position
        if len(angles)==0:
            gui.result_var.set("Please use Draw first.")
        else:
            angle = 360.0/n
            total_error = float(0.0)
            error = float(0.0)
            x_error = float(0.0)
            y_error = float(0.0)
            old_angle = float(0.0)
            old_bot_angle = float(0.0)
            rad_angle = float(0.0)
            rad_bot_angle = float(0.0)
            accumaltive_error = float(0.0)

            text2 = Text(root, height=30, width=80)
            scroll = Scrollbar(root, command=text2.yview)
            text2.configure(yscrollcommand=scroll.set)
            text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
            text2.tag_configure('big', font=('Verdana', 20, 'bold'))
            text2.tag_configure('color', foreground='#476042',
                                    font=('Arial', 10, 'bold'))
            text2.insert(END,'\nRobot Path Drawing Info\n', 'big')
            text2.insert(END, "Angle= %d, Length= %d\n"   % (angle, length), 'color')

            for i in range(n):
        #Drawing

                bot_length = length + randint(length/-10,length/10)   # length plus an error of +/- 10%
                bot_angle = ((angle // 10) * 10) + 10*randint(-1,1)
        #Calc errors
        # store BOTH old angles for summation

                old_bot_angle = old_bot_angle + bot_angle
                old_angle = old_angle + angle
                rad_angle = math.radians(old_angle)
                rad_bot_angle = math.radians(old_bot_angle)
                x_error = x_error + (length * math.sin(rad_angle) - bot_length * math.sin(rad_bot_angle))   # x component
                y_error = y_error + (length * math.cos(rad_angle) - bot_length * math.cos(rad_bot_angle))    # y component
                error = math.hypot(x_error, y_error)/length *100
                quote= "Bot_Angle= %d  Bot_Len= %d \n"  % (bot_angle, bot_length)
                e_position.append(error)
     #           quote= "Bot_Angle= %d  Bot_Len= %d  X_error= %.2f  Y_error= %.2f   Error= %.2f %% \n"  % (bot_angle, bot_length, x_error, y_error, error)
                #text2.insert(END, "Angle= %d, Length= %d\n"   % (angle, length), 'color')
                text2.insert(END, quote, 'color')
            quote=  "Drawing Error %.2f %% per the graphics\n" % (100*distance(0,0)/length)
            text2.insert(END, quote, 'color')
            text2.pack(side=LEFT)
            scroll.pack(side=RIGHT, fill=Y)




root = Tk()
root.wm_title('Robot Demostration GUI')
app = App(root)
root.mainloop()