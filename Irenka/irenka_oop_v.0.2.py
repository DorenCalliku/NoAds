###################################################################################
# Author: Doren Calliku
# Date: 4/29/2018
# Project: irenka
# Version: v.0.1.5
# References:
    # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    # http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html#updating-the-total
    # etc, many others
###################################################################################


import tkinter as tk
import time, random, datetime
from PIL import Image, ImageTk
from tkinter import font  as tkfont
from tkinter import *




class IrenkaApp(tk.Tk):
    """
        Main class forming basis for other classes to be called.
        Used to form the frame that will be used for the whole process.
    """

    def __init__(self, *args, **kwargs):
        # initialise base class
        tk.Tk.__init__(self, *args, **kwargs)

        # resizable = false so that people will not be able to resize because of the pictures that are not as moveable as one would want to.
        self.title("irenka")
        self.resizable(False, False)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        print(self)


        # create the basis container.
        container = tk.Frame(self,width=300, height=400) 	    # it is a frame
        container.grid()	# pack them on top of each other, fill the whole things, and expand accordingly.
        container.grid_rowconfigure(0, weight=1)				# row and column = 1
        container.grid_columnconfigure(0, weight=1)

        # DATA if needed to be used between different classes.
        # Apparently not useful if you put the classes into a stack because the frames work with screenshots in the beginning.
        # Suggestion : Update every 1 second - can help to connect the classes.
        self.frames = {}
        self.history = []
        self.answer_history = []

        # the frames are put in the loop.
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F( parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # start with this frame.
        self.show_frame("StartPage")
        #self.update_clock()
        #self.root.mainloop()


    def update_clock(self):
        self.root.after(1000, self.update_clock)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    """
        Presentation with IRENKA
        * Basic start: go either to settings or start playing.
    """

    def __init__(self, parent, controller):
        """
            Initialize everything that might be needed and be careful with resizing.
        """

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = Canvas(self)
        self.canvas.pack(fill = BOTH,expand = True)
        self.image = ImageTk.PhotoImage( file="C:/Users/Doren/Desktop/image.png")
        scale_w = 300 / self.image.width()
        scale_h = 400 / self.image.height()
        self.image.zoom(scale_w, scale_h)
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        """
        label = tk.Label(self, text="IRENKA", font=controller.title_font)
        label.grid(row=0,columnspan = 2)

        # image in the background
        # might be needed to change the whole thing into a canvas so that we can put buttons on the pictures.
        self.image 				= PhotoImage(file = "C:\\Users\\Doren\\Desktop\\pic.gif")
        self.background 		= Label(self, image=self.image)
        self.background.grid(row=1,columnspan= 2)

        #self.background.bind('<Configure>', self._resize_image)
        #self.pack(fill=BOTH, expand=YES)

        # buttons
        button1 = tk.Button(self,width= 15, text="Play", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self,width= 15, text="Settings", command=lambda: controller.show_frame("PageTwo"))
        button1.grid(row=2,column = 0)
        button2.grid(row=2,column = 1)

    # in case we need the resizing for further use.
    # It has the problem that it takes in the buttons.
    def _resize_image(self,event):
        new_width 	= event.width - 0
        new_height 	= event.height - 10
        self.image 	= self.img_copy.resize((new_width, new_height))
        self.background_image 			= ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
    """

class PageOne(tk.Frame):
    """
        The game.
        Write what one thinks into two simple lists and is expected to print them.
        In order to give the results we delete what we have produced.
        To be changed: Put both things on different pages so that it will become more manageable.
    """

    def __init__(self, parent, controller):
        """
            Constructor, start everything.
        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)

        # variables
        self.controller = controller
        self.name = StringVar()
        # DATA - choose the random word from these. To be extended or to be read from a file.
        # reading from a file ? check irenka.py
        self.lines = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family',
                 'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother',
                 'Mr', 'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question',
                 'right', 'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time',
                 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']
        self.word = StringVar
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # calculate the first word, print it and allow response.
        self.word   = (self.lines)[random.randint(0, len(self.lines) - 1)]
        self.label  = Label(self,text = "Enter your thoughts about {0}.".format(self.word))#, font = title_font)
        (self.label).grid(row=0, columnspan = 2)
        self.entry_box = tk.Entry(self, textvariable=(self.name), width=25, bg="lightgreen")
        (self.entry_box).grid(row=1, columnspan = 2)

        #
        # Enter-kind of a function. Remember the name for later.
        #
        def remember():
            """
            Register the words written for later presentation.
            :return: NULL
            """

            if len(str((self.name).get())) < 3:
                self.label_min_answer = Label(self, text="This cannot be accepted! Too small of an answer! \nIt is a game, but everything needs some sense of seriosity.\nWrite something meaningful.")
                (self.label_min_answer).grid(row=4, column=0)

            elif len(str((self.name).get())) >= 20:
                self.label.config(text="This cannot be accepted! Too big of an answer!\n What is your IQ by the way?\n Clean up your mess and write something meaningful.")

            else:
                # clear the entrybox, add the previous answer to the history
                (self.controller.answer_history).append(str((self.name).get()))
                self.word = (self.lines)[random.randint(0, len(self.lines) - 1)]
                (self.controller.history).append(str(self.word))

                (self.entry_box).delete(0, END)
                (self.entry_box).insert(0, "")
                (self.label).config(text=("Enter your thoughts about {0}.".format(self.word)))

        # finish the game.
        def finish():
            """
            End the game, enough you have played. Delete the previous widgets, write from beggining.
            Suggestion: Pass this function into a new class with its own presentation. (Not so crucial.)
            :return: NULL
            """
            self.entry_box.destroy()
            self.button_remember.destroy()
            self.button_finish.destroy()
            self.label_min_answer.destroy()

            if (len(self.controller.answer_history)) > 0:
                self.label.config(text = "Here are your pathetic thoughts! Stick to them. Best, Irenka.")
                string_history = StringVar()
                string_history = ""
                for i in range(1, len(self.controller.answer_history)):
                    string_history = string_history + "\n"+ self.controller.history[i]+ " | "+ self.controller.answer_history[i]
                    print(string_history)

                x = StringVar()
                x.set(string_history)
                label_x = Label(self, textvariable=x, padx = 10)
                label_x.grid(row=1,column = 0)

            else:
                self.label.config( text = "Take an economics course about decision making strategies in life.\n"
                                          "Next time you open this game you will know what to do.")



            def download(): return
            # download
            self.button_start = tk.Button(self, text="Download Your Thoughts", width=25, command=lambda: download)
            (self.button_start).grid(row=1,column = 0)

        self.button_remember = tk.Button(self, text="Remember",width=15, command=lambda: remember())
        self.button_finish   = tk.Button(self,   text="Finish",width=15, command = lambda: finish())
        (self.button_remember).grid(row=2,columnspan = 2)
        (self.button_finish).grid(row=3,columnspan = 2)

        # create global variables because of Button-call


class PageTwo(tk.Frame):
    """
    Settings page. It has the information needed from the whole game. It includes also the instructions.
    """
    def __init__(self, parent, controller):

        # TITLE
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Settings")
        self.label.grid(row = 0,columnspan = 2)

        # MUSIC
        """
        import pygame,os
        # threads are needed, check the idea of queue = python_gui_threads.py or https://makeapppie.com/2014/07/15/from-apple-to-raspberry-pi-how-to-do-threading-with-python-and-tkinter/
        # music @ constructor
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\Doren\\Desktop\\amy.wav")
        
        @ settings
        self.label_music = tk.Label(self, text="Do you want to listen to some music to chill your nerves?")
        self.label_music.grid(row=1,column = 0)

        def changeMusic():

            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True and self.music_var:
                continue



        self.music_var = StringVar()
        self.music_var = "OFF"
        self.check_music = tk.Checkbutton(self, text='Music',
                                command=changeMusic, variable=self.music_var,
                                onvalue='ON', offvalue='OFF')
        self.check_music.grid(row=1,column = 1)

        """


        # BACKGROUND
        self.label_background = tk.Label(self, text="Which background do you like for your game?")
        self.label_background.grid(row=2,column = 0)

        self.controller.background_var = StringVar()
        self.picture1 = tk.Radiobutton(self, text='Cathedral', variable=self.controller.background_var, value='Cathedral')
        self.picture2 = tk.Radiobutton(self, text='Water'    , variable=self.controller.background_var, value='Water')
        self.picture3 = tk.Radiobutton(self, text='None'     , variable=self.controller.background_var, value='None')
        self.picture1.grid(row=2,column = 1)
        self.picture2.grid(row=3,column = 1)
        self.picture3.grid(row=4,column = 1)

        # INSTRUCTIONS
        def showRules():
            messagebox.showinfo(title = "Game Rules", message="This will be a word-game which is based on one simple rule:\n say what you first thought, sincerely. \n " +
                        "The game will bring random words to you from a list of words.\n You have 10 seconds to write something.\n" +
                        "If 10 seconds pass your game finishes.\n" + "The word asked and your written text will be registered in a history.\n" +
                        "The history can be downloaded to your folder directly after the game is finished.\n" + "Honesty: Do not write meaningless words.")
        self.label_rules = tk.Label(self, text="Do you want to check the rules once?")
        self.label_rules.grid(row=5,column = 0)
        self.button_rules = tk.Button(self, text="Rules of the Game", width=15, command=lambda: showRules())
        self.button_rules.grid(row=5,column = 1)

        # PLAY
        self.label_play = tk.Label(self, text="If you finished you can go now to play.")
        self.label_play.grid(row=6,column = 0)
        self.button = tk.Button(self, text="Play", width=15, command=lambda: controller.show_frame("PageOne"))
        self.button.grid(row=6,column = 1)


if __name__ == "__main__":
    app = IrenkaApp()
    app.mainloop()