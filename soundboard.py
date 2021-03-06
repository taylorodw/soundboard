from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from playsound import playsound

# this first section makes our window and title
window = Tk()

window.geometry('290x475')

window.title("Soundboard")

lbl = Label(window, text="Soundboard", font=("Arial Bold", 18))

lbl.grid(columnspan=3, sticky=N, padx=5, pady=5)

from tkinter import *
from tkinter import filedialog
from tkinter import Menu

# making the functions for initializing, loading, and saving soundboards

def newboard():
    global onesound
    global twosound
    global threesound
    global foursound
    global fivesound
    global sixsound
    global sevensound
    global eightsound
    onesound = r"D:\Python\Soundboard\utility\silence.wav"
    twosound = r"D:\Python\Soundboard\utility\silence.wav"
    threesound = r"D:\Python\Soundboard\utility\silence.wav"
    foursound = r"D:\Python\Soundboard\utility\silence.wav"
    fivesound = r"D:\Python\Soundboard\utility\silence.wav"
    sixsound = r"D:\Python\Soundboard\utility\silence.wav"
    sevensound = r"D:\Python\Soundboard\utility\silence.wav"
    eightsound = r"D:\Python\Soundboard\utility\silence.wav"

def loadboard():
    global onesound
    global twosound
    global threesound
    global foursound
    global fivesound
    global sixsound
    global sevensound
    global eightsound
    loadname = filedialog.askopenfilename()
    boardfile = open(loadname, "r")
    onepath = boardfile.readline()
    onesound = onepath.rstrip()
    twopath = boardfile.readline()
    twosound = twopath.rstrip()
    threepath = boardfile.readline()
    threesound = threepath.rstrip()
    fourpath = boardfile.readline()
    foursound = fourpath.rstrip()
    fivepath = boardfile.readline()
    fivesound = fivepath.rstrip()
    sixpath = boardfile.readline()
    sixsound = sixpath.rstrip()
    sevenpath = boardfile.readline()
    sevensound = sevenpath.rstrip()
    eightpath = boardfile.readline()
    eightsound = eightpath.rstrip()
    boardfile.close()



def saveboard():
    global onesound
    global twosound
    global threesound
    global foursound
    global fivesound
    global sixsound
    global sevensound
    global eightsound
    savename = filedialog.asksaveasfilename()
    savefile = open(savename, "w")
    soundlist = [onesound, twosound, threesound, foursound, fivesound, sixsound, sevensound, eightsound]
    savefile.write('\n'.join(soundlist))
    savefile.close()


# making the menu, with save and load features
menu = Menu(window)

new_item = Menu(menu, tearoff=0)

new_item.add_command(label='New soundboard', command=newboard)
new_item.add_command(label='Load soundboard', command=loadboard)
new_item.add_command(label='Save soundboard', command=saveboard)

menu.add_cascade(label='Menu', menu=new_item)

window.config(menu=menu)

# playsound doesn't work unless a .wav is loaded, so i load a short silent .wav file
# users will need to change the filepath for now, eventually this should be all onboard
onesound = r"D:\Python\Soundboard\utility\silence.wav"
twosound = r"D:\Python\Soundboard\utility\silence.wav"
threesound = r"D:\Python\Soundboard\utility\silence.wav"
foursound = r"D:\Python\Soundboard\utility\silence.wav"
fivesound = r"D:\Python\Soundboard\utility\silence.wav"
sixsound = r"D:\Python\Soundboard\utility\silence.wav"
sevensound = r"D:\Python\Soundboard\utility\silence.wav"
eightsound = r"D:\Python\Soundboard\utility\silence.wav"



# these are the functions for each button. they trigger when clicked
def oneloadclicked():
    global onesound
    onesound = filedialog.askopenfilename()

def oneclicked():
    playsound(onesound)

def twoloadclicked():
    global twosound
    twosound = filedialog.askopenfilename()

def twoclicked():
    playsound(twosound)

def threeloadclicked():
    global threesound
    threesound = filedialog.askopenfilename()

def threeclicked():
    playsound(threesound)

def fourloadclicked():
    global foursound
    foursound = filedialog.askopenfilename()

def fourclicked():
    playsound(foursound)

def fiveloadclicked():
    global fivesound
    fivesound = filedialog.askopenfilename()

def fiveclicked():
    playsound(fivesound)

def sixloadclicked():
    global sixsound
    sixsound = filedialog.askopenfilename()

def sixclicked():
    playsound(sixsound)

def sevenloadclicked():
    global sevensound
    sevensound = filedialog.askopenfilename()

def sevenclicked():
    playsound(sevensound)

def eightloadclicked():
    global eightsound
    eightsound = filedialog.askopenfilename()

def eightclicked():
    playsound(eightsound)

# this part tells tkinter to draw each button and link them back to the functions above
one = Button (window, text="1", command=oneclicked)
one.config(height=5, width=10)
one.grid(column=0, row=1, padx=5, pady=5)

oneload = Button (window, text ="Load 1", command=oneloadclicked)
oneload.config(height=2, width=5)
oneload.grid(column=1, row=1, padx=5, pady=5)

two = Button (window, text="2", command=twoclicked)
two.config(height=5, width=10)
two.grid(column=2, row=1, padx=5, pady=5)

twoload = Button (window, text ="Load 2", command=twoloadclicked)
twoload.config(height=2, width=5)
twoload.grid(column=3, row=1, padx=5, pady=5)

three = Button (window, text="3", command=threeclicked)
three.config(height=5, width=10)
three.grid(column=0, row=3, padx=5, pady=5)

threeload = Button (window, text ="Load 3", command=threeloadclicked)
threeload.config(height=2, width=5)
threeload.grid(column=1, row=3, padx=5, pady=5)

four = Button (window, text="4", command=fourclicked)
four.config(height=5, width=10)
four.grid(column=2, row=3, padx=5, pady=5)

fourload = Button (window, text ="Load 4", command=fourloadclicked)
fourload.config(height=2, width=5)
fourload.grid(column=3, row=3, padx=5, pady=5)

five = Button (window, text="5", command=fiveclicked)
five.config(height=5, width=10)
five.grid(column=0, row=5, padx=5, pady=5)

fiveload = Button (window, text ="Load 5", command=fiveloadclicked)
fiveload.config(height=2, width=5)
fiveload.grid(column=1, row=5, padx=5, pady=5)

six = Button (window, text="6", command=sixclicked)
six.config(height=5, width=10)
six.grid(column=2, row=5, padx=5, pady=5)

sixload = Button (window, text ="Load 6", command=sixloadclicked)
sixload.config(height=2, width=5)
sixload.grid(column=3, row=5, padx=5, pady=5)

seven = Button (window, text="7", command=sevenclicked)
seven.config(height=5, width=10)
seven.grid(column=0, row=7, padx=5, pady=5)

sevenload = Button (window, text ="Load 7", command=sevenloadclicked)
sevenload.config(height=2, width=5)
sevenload.grid(column=1, row=7, padx=5, pady=5)

eight = Button (window, text="8", command=eightclicked)
eight.config(height=5, width=10)
eight.grid(column=2, row=7, padx=5, pady=5)

eightload = Button (window, text ="Load 8", command=eightloadclicked)
eightload.config(height=2, width=5)
eightload.grid(column=3, row=7, padx=5, pady=5)

window.mainloop()
