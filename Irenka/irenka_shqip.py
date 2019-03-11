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

# create main window, menubar and canvas. Remember: For canvas you will do the adding manually
master = Tk()
master.title("irenka")
master.geometry('%dx%d+0+0' % (400,400))
master.resizable(False,False)
menubar = Menu(master)
canvas = Canvas(master)
master.config(menu=menubar)
canvas.pack(expand=True, fill=BOTH)

# Background
def updateBackground():
    pictures = []
    i = 0
    pictures.append("pic(1).gif")
    pictures.append("pic(2).gif")
    image1 = PhotoImage(file=pictures[0])
    canvas.img = image1
    canvas.create_image(0, 0, anchor=NW, image=image1)
    def changeBackground( x):
        global image1, canvas, pictures, i
        i = (i+x)% (len(pictures))
        image1 = PhotoImage(file=pictures[i])
        canvas.img = image1
        canvas.create_image(0,0, anchor=NW,image=image1)

updateBackground()


timer_change = 1
timer_var = 10
label_timer_x= "Koha qe te lejohet te pergjigjesh eshte {0} sekonda.".format(timer_var)
label_text_timer_x = StringVar()
label_text_timer_x.set(label_timer_x)
label_timer_xy = Label(canvas, textvariable=label_text_timer_x)
canvas.create_window(25, 350, window=label_timer_xy, anchor=NW)

def changeTimer(x):
    # change the timing of the game

    global timer_var,label_timer_x
    timer_var = timer_var + int(x)

    if timer_var < 6 or timer_var > 20:
           messagebox.showinfo(title="Nuk lejohet",
                        message="Keto kushte qe keni zgjedhur per kohen nuk lejohen")
    else:
        label_timer_x = "Koha qe te lejohet te pergjigjesh eshte {0} sekonda.".format(timer_var)
        label_text_timer_x.set(label_timer_x)



"""
# read from file
text_file   = open("words.txt", "r")
lines       = text_file.read().split()
text_file.close()
"""
#
# create global variables to be used for the information flow
#
word = StringVar
history = []
answer_history = []
lines = ["atdheu", "rrezik","atëherë","njerëzit","padijshëm","filloj","mendoj","ara","varri","prish","fole","bilbil","shikoj","nena","harroj","të gjitha","e huaj","mjalte","bijë","vendim","argjend","bukë","shtëpi","vater","komb","vlere","zog","dardha","derë","bota","strehë","shqiponje"]
timer = timer_var

#
# Play method.
#
def play():

    global x,word,lines,history,answer_history,timer
    button_play.destroy()
    label_timer_xy.destroy()

    # start the game
    x = random.randint(0, len(lines) - 1)
    word = lines[x]
    del lines[x]

    # print everything
    label_message = "Shkruaj mendimet e tua ne lidhje me {0}.".format(word)
    label_text = StringVar()
    label_text.set(label_message)
    label = Label(canvas, textvariable=label_text)
    canvas.create_window(25,25, window=label, anchor=NW)

    label_message_max = "Kjo nuk mund te pranohet! Pergjigje shume e gjate!   \nCfare inteligjence ke ti meqe ra llafi?\nShkruaj dicka te mbledhur edhe te kuptimte."
    label_message_min = "Kjo nuk mund te pranohet! Pergjigje shume e shkurter! \nCfare inteligjence ke ti meqe ra llafi?\nEshte nje loje, kuptohet, por ka nevoje per nje sens serioziteti"

    def showMessage(title,message):
        messagebox.showinfo(title=title, message=message)

    def remember():
        global word,lines,x,answer_history,history,timer
        if len(str(name.get())) < 3:
           showMessage("Pergjigje e shkurter",label_message_min)


        elif len(str(name.get())) >= 20:
            showMessage("Pergjigje e gjate", label_message_max)

        else:
            if len(lines)< 1:
                history.append(str(word))
                answer_history.append(str(name.get()))
                label_message_end = "Sapo mbarove te gjitha fjalet qe kemi ne fjalor. Pergezime."
                showMessage("I nxorre fundin Jake",label_message_end)
                finish()

            else :

                history.append(str(word))
                answer_history.append(str(name.get()))
                entry_box.delete(0, END)
                entry_box.insert(0, "")

                x = random.randint(0, len(lines) - 1)
                word = lines[x]
                del lines[x]

                label_message = "Shkruaj mendimet e tua ne lidhje me {0}.".format(word)
                label_text.set(label_message)

                # reset the clock
                timer = timer_var



    def finish():
        entry_box.destroy()
        button_remember.destroy()
        button_finish.destroy()
        label_timer.destroy()
        global timer_change
        timer_change = 0

        if len(answer_history) > 0:
            label_message = "Keto jane mendimet e tua patetike ne lidhje me temat e shkruara.\nPranoji dhe behu nje me to.\nMe te mirat, Irenka."
            label_text.set(label_message)
            string_history = ""
            for i in range(0, len(answer_history)):
                if i == 0 :
                    string_history = ('{0} - {1}\n'.format(history[i], answer_history[i]))
                elif i <(len(answer_history)-1):
                    string_history = string_history +('{0} - {1}\n'.format( history[i],answer_history[i]))
                    print(string_history)
                    #string_history = string_history + "\n" + history[i] + " | " + answer_history[i]
                else:
                    string_history = string_history + ('{0} - {1}'.format(history[i], answer_history[i]))
            x = StringVar()
            x.set(string_history)
            label_x = Label(canvas, textvariable=x, padx=10)
            canvas.create_window(125, 100, window=label_x, anchor=NW)

        else:
            label_message = "Duhet te marresh disa mesime nga \nlenda e ekonomise ne lidhje me vendimarrjen."
            label_text.set(label_message)


    #
    # Working on timer
    #
    global timer
    timer = timer_var
    label_message_timer = "Edhe {0} sekonda te kane mbetur te pergjigjesh.".format(timer)
    label_text_timer = StringVar()
    label_text_timer.set(label_message_timer)
    label_timer = Label(canvas, textvariable=label_text_timer)
    canvas.create_window(25, 350, window=label_timer, anchor=NW)

    def clock():
        global timer,timer_change
        timer -= timer_change
        label_message_timer = "Edhe {0} sekonda te kane mbetur te pergjigjesh.".format(timer)
        label_text_timer.set(label_message_timer)

        if timer <= 0:
            showMessage("Koha mbaroi","Ki kujdes kohen heren tjeter.\nNese te duhet me shume kohe per tu menduar shko te Cilesimet.")
            finish()
        else:
            master.after(1000, clock)  # run itself again after 1000 ms

    clock()

    def remember_triger(event):
        remember()

    name = StringVar()
    entry_box = Entry(master, textvariable=name, width=25, bg="lightgreen")
    canvas.create_window(25, 50, window=entry_box, anchor=NW)
    entry_box.focus()

    button_remember = Button(canvas, text="Ruaje", width=10, height=1, command=remember)
    button_finish   = Button(canvas, text="Mbaro",   width=10, height=1, command=finish)
    canvas.create_window(25, 75, window=button_remember, anchor=NW)
    canvas.create_window(25, 105, window=button_finish, anchor=NW)
    master.bind('<Return>', remember_triger)





def showRules():
    messagebox.showinfo(title="Rregullat e lojes",
                        message="Loja eshte goxha e thjeshte.\nShkruaj cfare te vjen ndermend direkt.\nPerpiqu te jesh i sinqerte.")

def showAbout():
    messagebox.showinfo(title="Mbi ne",
                        message="Irenka - Versioni V.0.2 (Me Menubar)\n"+
                                "Irenka eshte nje loje e gjendur nga Irena Caushi."+
                                "Programuesi i lojes eshte Doren Calliku.")

def showHelp():
    messagebox.showinfo(title="Ndihme",
                        message="Rifillo e nis lojen nga fillimi duke fshire historine.\nMbylle mbaron lojen dhe del.\nNese keni ndonje sugjerim apo ndonje problem mund te kontaktoni me ane te emailit: dcalliku@gmail.com.")

def restart():
    global history, answer_history
    history = []
    answer_history = []
    canvas.delete("all")
    updateBackground()
    play()


# position by hand
button_play = tk.Button(canvas, width=15, text="Luaj", command= play )
canvas.create_window(120,140, window=button_play, anchor=NW)


# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Rifillo", command=restart)
filemenu.entryconfig(1, state=DISABLED)
filemenu.add_separator()
filemenu.add_command(label="Sfondi paraardhes", command=lambda :changeBackground(1))
filemenu.add_command(label="Sfondi pasardhes", command=lambda :changeBackground(-1))
filemenu.add_separator()
filemenu.add_command(label="Zvogelo kohen -2", command=lambda :changeTimer(-2))
filemenu.add_command(label="Shto kohen +2", command=lambda :changeTimer(2))
filemenu.add_separator()
filemenu.add_command(label="Mbylle",    command=master.quit)
menubar.add_cascade(label="Loja", menu=filemenu)



# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Rregullat", command=showRules)
editmenu.add_separator()
editmenu.add_command(label="Ndihme",command= showHelp)
menubar.add_cascade(label="Informacion", menu=editmenu)


#
# Start the game.
#
master.config(menu=menubar)
master.mainloop()