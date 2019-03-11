###################################################################################
# Author: Doren Calliku
# Date: 11/5/2018
# Project: irenka
# Version: v.0.2
# Type: MenuBar
###################################################################################



from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import time, random

# create main window, make it not-resizable.
master = Tk()
master.title("irenka")
master.geometry('%dx%d+0+0' % (400, 300))
master.resizable(False,False)



# create menubar and canvas. Remember: For canvas you will do the adding manually
menubar = Menu(master)
canvas = Canvas(master)
canvas.pack(expand=True, fill=BOTH)

#image = Image.open('File.jpg')
#image.show()
# add picture to canvas
pictures = []
i = 0
pictures.append("C:/Users/Doren/Desktop/pic.gif")
pictures.append("C:/Users/Doren/Desktop/pic1.gif")
pictures.append("C:/Users/Doren/Desktop/pic2.gif")
pictures.append("C:/Users/Doren/Desktop/pic3.gif")
print(pictures)
image1 = PhotoImage(file=pictures[0])
canvas.img = image1
canvas.create_image(0, 0, anchor=NW, image=image1)


"""
label_heading = Label(master, text="Hey! This is Irena's simple game.\n")
label_heading.configure(background='orange')
label_rules = Label(master, text="Respond with the first thought that comes to your mind.\n ")
label_rules.configure(background='orange')
label_heading.pack()
label_rules.pack()
"""

# create global variables because of Button-call
word = StringVar
history = []
answer_history = []

# function used for menubar
def changeBackground():
    global image1, canvas, pictures, i
    i = (i+1)% len(pictures)
    image1 = PhotoImage(file=pictures[i])
    canvas.img = image1
    canvas.create_image(0,0, anchor=NW,image=image1)
#
# Main method of the game. It starts everything.
#
def play():
    '''The game.'''
    # destroy previous layout
    button_play.destroy()

    # read from file
    # text_file   = open("words.txt", "r")
    # lines       = text_file.read().split()
    # text_file.close()

    lines = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family',
             'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr',
             'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room',
             'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman',
             'word', 'work', 'world', 'year']


    # start the game
    word = lines[random.randint(0, len(lines) - 1)]
    history.append(str(word))

    # print everything
    label_message = "Enter your thoughts about {0}.".format(word)
    label_text = StringVar()
    label_text.set(label_message)
    label = Label(canvas, textvariable=label_text)
    canvas.create_window(25,25, window=label, anchor=NW)

    label_message_max = "This cannot be accepted! Too big of an answer!   \nWhat is your IQ by the way?\nClean up your mess and write something meaningful."
    label_message_min = "This cannot be accepted! Too small of an answer! \nWhat is your IQ by the way?\nIt is a game, but everything needs some sense of seriosity.\nWrite something meaningful."
    def showMessage(title,message):
        messagebox.showinfo(title=title, message=message)

    def remember():

        if len(str(name.get())) < 3:
           showMessage("Small Answer",label_message_min)


        elif len(str(name.get())) >= 20:
            showMessage("Big Answer", label_message_max)

        else:
            word = lines[random.randint(0, len(lines) - 1)]
            history.append(str(word))
            answer_history.append(str(name.get()))
            label_message = "Enter your thoughts about {0}.".format(word)
            label_text.set(label_message)
            entry_box.delete(0, END)
            entry_box.insert(0, "")



    def finish():
        entry_box.destroy()
        button_remember.destroy()
        button_finish.destroy()

        if len(answer_history) > 0:
            label_message = "Here are your pathetic thoughts! Stick to them. Best, Irenka."
            label_text.set(label_message)
            string_history = ""
            for i in range(0, len(answer_history)):
                if i != 0 :
                    string_history = string_history + "\n" + history[i] + " | " + answer_history[i]
                else:
                    string_history = history[i] + " | " + answer_history[i]
            x = StringVar()
            x.set(string_history)
            label_x = Label(master, textvariable=x, padx=10)
            canvas.create_window(25, 75, window=label_x, anchor=NW)


        else:
            label_message = "Take an economics course about decision making strategies in life.\nNext time you open this game you will know what to do. "
            label_text.set(label_message)

    name = StringVar()
    entry_box = Entry(master, textvariable=name, width=25, bg="lightgreen")
    canvas.create_window(25, 50, window=entry_box, anchor=NW)

    # lambda: controller.show_frame("StartPage")
    button_remember = Button(canvas, text="Remember", width=10, height=1, command=remember)
    button_finish   = Button(canvas, text="Finish",   width=10, height=1, command=finish)
    canvas.create_window(25, 75, window=button_remember, anchor=NW)
    canvas.create_window(25, 105, window=button_finish, anchor=NW)
    # button      = Button(master, text="Good-bye.", command=master.destroy).place(x=0,y=150)


def changeSettings():
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    checkButton_Music = Checkbutton(master, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=25)
    checkButton_Background = Checkbutton(master, text="Background", variable=CheckVar2, onvalue=1, offvalue=0, height=5,
                                         width=25)
    checkButton_Background.pack()
    checkButton_Music.pack()


def showRules():
    messagebox.showinfo(title="Game Rules",
                        message="This will be a word-game which is based on one simple rule:\n say what you first thought, sincerely. \n " +
                                "The game will bring random words to you from a list of words.\n You have 10 seconds to write something.\n" +
                                "If 10 seconds pass your game finishes.\n" + "The word asked and your written text will be registered in a history.\n" +
                                "The history can be downloaded to your folder directly after the game is finished.\n" + "Honesty: Do not write meaningless words.")

def showAbout():
    messagebox.showinfo(title="About",
                        message="Irenka - Version V.0.2 (Menubar)\n"+
                                "Irenka is a game introduced by Irena Caushi."+
                                "The programmer of the game is Doren Calliku")

def showHelp():
    messagebox.showinfo(title="Help",
                        message="Restart deletes the history.\nExit kills the application.\n If you have any suggestions or have problems email to dcalliku@gmail.com.")

def restart():
    global history, answer_history
    history = []
    answer_history = []


# position by hand
button_play = tk.Button(canvas, width=15, text="Play", command= play )
canvas.create_window(120,140, window=button_play, anchor=NW)


# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=restart)
filemenu.add_command(label="Change Background", command=changeBackground)
filemenu.add_separator()
filemenu.add_command(label="Exit",    command=master.quit)
menubar.add_cascade(label="Game", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Rules", command=showRules)
editmenu.add_separator()
editmenu.add_command(label="Help",command= showHelp)
menubar.add_cascade(label="Info", menu=editmenu)




# display the menu
master.config(menu=menubar)

master.mainloop()