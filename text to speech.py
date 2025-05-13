from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.configure(bg="ghostwhite")
root.title("Anand's - TExt to Speech")

Label(root, text="Text to Speech", font="arial 20 bold", bg="white smoke").pack()
Label(root, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)

Msg = StringVar()
Label(root, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)
entry_field = Entry(root, textvariable=Msg, width=100)
entry_field.place(x=20, y=100)
def Text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save("anand.mp3")
    playsound("anand.mp3")

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text="Play", font="arial 15 bold", bg="light green", command=Text_to_speech).place(x=20, y=140)
Button(root, text="Reset", font="arial 15 bold", bg="light blue", command=Reset).place(x=100, y=140)
Button(root, text="Exit", font="arial 15 bold", bg="light coral", command=Exit).place(x=200, y=140)
root.mainloop()