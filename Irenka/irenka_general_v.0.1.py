###################################################################################
# Author: Doren Calliku
# Date: 4/29/2018
# Project: irenka
# Version: v.0.1.0
# References:
    # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    # http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html#updating-the-total
    #
###################################################################################

from tkinter import *
import tkinter as tk
import time, random

root=Tk()
root.title("irenka")

#C = Canvas(root, bg="blue", height=250, width=300)
#filename  = PhotoImage(file = "C:\\Users\\Doren\\Desktop\\flowers.gif")
#filename2 = PhotoImage(file = "C:\\Users\\Doren\\Desktop\\beach.2.gif")
#filename3 = PhotoImage(file = "C:\\Users\\Doren\\Desktop\\path1.gif")
background_label = Label(root, bg = "orange")#, image=filename3)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry('%dx%d+0+0' % (400,400))
label_heading   = Label(root, text = "Hey! This is Irena's simple game.\n")
label_heading.configure(background='orange')
label_rules     = Label(root, text="Respond with the first thought that comes to your mind.\n ")
label_rules.configure(background = 'orange')
label_heading.pack()
label_rules.pack()


#
# Main method of the game. It starts everything.
#
def play():
    '''The game.'''
    # destroy previous layout
    label_heading.destroy()
    label_rules.destroy()
    button_play.destroy()

    # read from file
    #text_file   = open("words.txt", "r")
    #lines       = text_file.read().split()
    #text_file.close()
    #print(lines)
    lines = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family', 'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr', 'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']

    # create global variables because of Button-call
    word            = StringVar
    history         = []
    answer_history  = []

    # start the game
    word    = lines[random.randint(0, len(lines)-1)]
    history.append(str(word))

    # print everything
    label_message     = "Enter your thoughts about {0}.".format(word)
    label_text  = StringVar()
    label_text.set(label_message)
    label       = Label(root, textvariable=label_text)
    label.configure(background='orange')
    label.pack()

    def remember():

        if len(str(name.get())) < 3:
            #print("This cannot be accepted! Too small of an answer! What is your IQ by the way?")
            label_message = "This cannot be accepted! Too small of an answer! \nIt is a game, but everything needs some sense of seriosity.\nWrite something meaningful."
            #label_text    = StringVar()
            label_text.set(label_message)
            label.configure(background='orange')
            #label = Label(root,textvariable= label_text)
            #label.pack()

        elif len(str(name.get())) >= 20:
            label_message = "This cannot be accepted! Too big of a string!\n What is your IQ by the way?\n Clean Up your mess and write something meaningful."
            label_text.set(label_message)
			
        else:
            word = lines[random.randint(0, len(lines)-1)]
            history.append(str(word))
            answer_history.append(str(name.get()))
            label_message = "Enter your thoughts about {0}.".format(word)
            label_text.set(label_message)

    def finish():
        entry_box.destroy()
        button_remember.destroy()
        button_finish.destroy()

        if len(answer_history) > 0:
            label_message = "Here are your pathetic thoughts! Stick to them. Best, Irenka."
            label_text.set(label_message)
            string_history = ""
            print(len(answer_history))
            for i in range(0, len(answer_history)):
                string_history = string_history + "\n"+ history[i]+ " | "+ answer_history[i]

            x = StringVar()
            x.set(string_history)
            label_x=Label(root, textvariable=x, padx = 10)
            label_x.pack()
            label_x.configure(background='orange')

        else:
            label_message = "Take an economics course about decision making strategies in life.\nNext time you open this game you will know what to do. "
            label_text.set(label_message)

    name        = StringVar()
    entry_box   = Entry( root, textvariable = name, width = 25, bg = "lightgreen")
    entry_box.pack()

    #lambda: controller.show_frame("StartPage")
    button_remember    = Button(root,    text ="Remember", width = 10,bg="lightgreen", height = 1, command=  remember)
    button_finish      = Button(root,      text ="Finish", width = 10,bg="lightgreen", height = 1, command=    finish)
    button_remember.pack()
    button_finish.pack(side=BOTTOM)
    #button      = Button(root, text="Good-bye.", command=root.destroy).place(x=0,y=150)

button_play = tk.Button(root,width =25, text="Play",bg="lightgreen", fg="black", command= play )
button_play.pack()

mainloop()
