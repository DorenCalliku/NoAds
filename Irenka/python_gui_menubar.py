from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import time, random

master = Tk()
master.title("irenka")
master.geometry('%dx%d+0+0' % (400, 400))
master.resizable(False,False)

menubar = Menu(master)
canvas = Canvas(master)
canvas.pack(expand=True, fill=BOTH)
image1 = PhotoImage(file="C:/Users/Doren/Desktop/pic.gif")
# keep a link to the image to stop the image being garbage collected
canvas.img = image1
canvas.create_image(0, 0, anchor=NW, image=image1)


def hello():
    print("hello!")



button1 = tk.Button(canvas, width=15, text="Play", command=master.destroy)
canvas.create_window(130,160, window=button1, anchor=NW)

label_heading = Label(master, text="Hey! This is Irena's simple game.\n")
label_heading.configure(background='orange')
label_rules = Label(master, text="Respond with the first thought that comes to your mind.\n ")
label_rules.configure(background='orange')
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
    # text_file   = open("words.txt", "r")
    # lines       = text_file.read().split()
    # text_file.close()
    # print(lines)
    lines = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family',
             'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr',
             'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room',
             'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman',
             'word', 'work', 'world', 'year']

    # create global variables because of Button-call
    word = StringVar
    history = []
    answer_history = []

    # start the game
    word = lines[random.randint(0, len(lines) - 1)]
    history.append(str(word))

    # print everything
    label_message = "Enter your thoughts about {0}.".format(word)
    label_text = StringVar()
    label_text.set(label_message)
    label = Label(master, textvariable=label_text)
    label.configure(background='orange')
    label.pack()

    def remember():

        if len(str(name.get())) < 3:
            # print("This cannot be accepted! Too small of an answer! What is your IQ by the way?")
            label_message = "This cannot be accepted! Too small of an answer! \nIt is a game, but everything needs some sense of seriosity.\nWrite something meaningful."
            # label_text    = StringVar()
            label_text.set(label_message)
            label.configure(background='orange')
            # label = Label(master,textvariable= label_text)
            # label.pack()

        elif len(str(name.get())) >= 20:
            label_message = "This cannot be accepted! Too big of a string!\n What is your IQ by the way?\n Clean Up your mess and write something meaningful."
            label_text.set(label_message)

        else:
            word = lines[random.randint(0, len(lines) - 1)]
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
                string_history = string_history + "\n" + history[i] + " | " + answer_history[i]

            x = StringVar()
            x.set(string_history)
            label_x = Label(master, textvariable=x, padx=10)
            label_x.pack()
            label_x.configure(background='orange')

        else:
            label_message = "Take an economics course about decision making strategies in life.\nNext time you open this game you will know what to do. "
            label_text.set(label_message)

    name = StringVar()
    entry_box = Entry(master, textvariable=name, width=25, bg="lightgreen")
    entry_box.pack()

    # lambda: controller.show_frame("StartPage")
    button_remember = Button(master, text="Remember", width=10, bg="lightgreen", height=1, command=remember)
    button_finish = Button(master, text="Finish", width=10, bg="lightgreen", height=1, command=finish)
    button_remember.pack()
    button_finish.pack(side=BOTTOM)
    # button      = Button(master, text="Good-bye.", command=master.destroy).place(x=0,y=150)


def changeSettings():
    button_play = tk.Button(master, width=25, text="Play", bg="lightgreen", fg="black", activeforeground="green",
                            command=play)
    button_play.pack()
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



# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=hello)
filemenu.add_command(label="Pause", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Change Background", command=hello)
editmenu.add_command(label="Show Rules", command=showRules)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
master.config(menu=menubar)

master.mainloop()