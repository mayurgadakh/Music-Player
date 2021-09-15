import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from pygame import *
from pygame import mixer
import os
from tkinter import filedialog
from tkinter import messagebox

current_volume = float(0.5)


def addsongs():
    global songs
    songs = filedialog.askopenfilenames(
        initialdir='D:/', title="Choose Songs", filetypes=(("mp3 Files", "*.mp3"), ))
    global song
    for song in songs:
        playlist.insert(END,song)


def playsong():
    try:
        currentsong = playlist.get(ACTIVE)
        mixer.music.load(currentsong)
        mixer.music.set_volume(current_volume)
        songstatus.set("Playing")
        mixer.music.play()
        global songtitle
        songtitle = song.split("/")
        songtitle = songtitle[-1]
        c = currentsong.split("/")
        c=c[-1]
        NPLabel = tk.Label(root, text=currentsong)
        NPLabel["font"] = tkFont.Font(family='Helvetica', size=10)
        NPLabel["fg"] = "#333333"
        NPLabel["justify"] = "left"
        NPLabel.place(x=10, y=510, width=300, height=38)
        NPLabel.config(fg="green", text="Now Playing: " + str(c))
    except Exception as q:
        messagebox.showwarning("No Songs Added!", "Please click on add songs to add songs to play!")


def reduce_volume():
    try:
        global current_volume
        if current_volume ==0:
            vollabel.config(fg="black",text="V:Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        vollabel.config(text="V: "+str(current_volume))
    except Exception as e:
        pass

def increase_volume():
    try:
        global current_volume
        if current_volume ==1:
            vollabel.config(fg="black", text="V:Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        vollabel.config(text="V: "+str(current_volume))
    except Exception as e:
        pass
    


def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()


def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()


def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

def myinfo():
    messagebox.showinfo("About","Designed and Developed by Mayur Gadakh")

root = Tk()
root.title('Music Player')
root.resizable(height=False, width=False)
width = 1000
height = 562
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.iconbitmap("./icon.ico")

bg = PhotoImage(file="./bgimage.gif")
canvas1 = Canvas(root, width=1280, height=720)

canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg, anchor="nw")


mixer.init()
songstatus = StringVar()
songstatus.set("Choosing")

menubar = Menu(root)
root.config(menu=menubar)

add_song_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Songs", command=addsongs)

aboutmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About",command=myinfo)

playbtn = Button(root)
playbtn["bg"] = "#c4939c"
playbtn["cursor"] = "arrow"
playbtn["font"] = tkFont.Font(family='Helvetica', size=15)
playbtn["fg"] = "#000000"
playbtn["justify"] = "center"
playbtn["text"] = "Play"
playbtn["relief"] = "raised"
playbtn.place(x=460, y=490, width=80, height=55)
playbtn["command"] = playsong

playlist = Listbox(root, selectmode=SINGLE)
playlist["bg"] = "#e3b1bb"
playlist["borderwidth"] = "3px"
playlist["font"] = tkFont.Font(family='Helvetica', size=15)
# playlist["fg"] = "#333333"
playlist["justify"] = "left"
playlist["relief"] = "raised"
playlist["selectbackground"] = "#90f090"
playlist.place(x=0, y=0, width=1000, height=490)

pausebtn = tk.Button(root)
pausebtn["bg"] = "#c4939c"
pausebtn["font"] = tkFont.Font(family='Helvetica', size=15)
pausebtn["fg"] = "#000000"
pausebtn["justify"] = "center"
pausebtn["text"] = "Pause"
pausebtn.place(x=540, y=490, width=70, height=55)
pausebtn["command"] = pausesong

stopbtn = tk.Button(root)
stopbtn["bg"] = "#c4939c"
stopbtn["font"] = tkFont.Font(family='Helvetica', size=15)
stopbtn["fg"] = "#000000"
stopbtn["justify"] = "center"
stopbtn["text"] = "Stop"
stopbtn.place(x=390, y=490, width=70, height=55)
stopbtn["command"] = stopsong

minusVbtn = tk.Button(root)
minusVbtn["bg"] = "#c4939c"
minusVbtn["font"] = tkFont.Font(family='Times', size=10)
minusVbtn["fg"] = "#000000"
minusVbtn["justify"] = "center"
minusVbtn["text"] = "-V"
minusVbtn.place(x=850, y=490, width=45, height=55)
minusVbtn["command"] = reduce_volume

plusVbtn = tk.Button(root)
plusVbtn["bg"] = "#c4939c"
plusVbtn["font"] = tkFont.Font(family='Times', size=10)
plusVbtn["fg"] = "#000000"
plusVbtn["justify"] = "center"
plusVbtn["text"] = "+V"
plusVbtn.place(x=950, y=490, width=45, height=55)
plusVbtn["command"] = increase_volume

vollabel = Label(fg="green", text="Volume : " + str(current_volume))
vollabel.config(text="V: "+str(current_volume),bg="green",fg="black")
vollabel.place(x=900,y=505)


mainloop()




