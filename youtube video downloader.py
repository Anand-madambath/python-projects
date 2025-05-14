from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("600x400")
root.resizable(0, 0)
root.title("YouTube Video Downloader")
link= StringVar()
Label(root, text="YouTube Video Downloader", font="arial 20 bold").pack()
link_enter = Entry(root, width=70,textvariable=link).place(x=32, y=70)
def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="arial 15").place(x=200, y=200)
Button(root, text="Download", font="arial 15", bg="lightblue", command=download).place(x=200, y=150)
root.mainloop()