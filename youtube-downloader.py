from tkinter import *
from tkinter import filedialog
import pytube
from pytube import YouTube
import threading


root = Tk()
root.title("Youtube Downloader")
root.geometry("600x320")
root.resizable(False,False)


def browse():
    directory =filedialog.askdirectory(title="save video")
    folderLink.delete(0,"end")
    folderLink.insert(0,directory)

def download():
    status.config(text="Dowloading")
    link = ytlink.get()
    folderLink.get()
    YouTube(link,on_complete_callback=finish).streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first().download(folderLink.get())
    

def finish (stream=None ,chunk=None ,file_handle=None ,remaining=None):
    status.config(text="Complete")

ytLogo = PhotoImage(file='logo.png').subsample(2)
ytTitle =Label(root, image=ytLogo)
ytTitle.place( relx=0.5, rely=0.25 , anchor="center")
 
ytlabel = Label(root ,text="Youtube Link")
ytlabel.place(x=25 ,y=150)

ytlink = Entry(root , width=60)
ytlink.place(x=140,y=150)

folderLabel = Label(root , text="Download Folder")
folderLabel.place(x=25 , y=183)

folderLink= Entry(root,width=50)
folderLink.place(x=140 , y=183)

browse = Button(root,text="Browse" ,command=browse)
browse.place(x=455,y=180)

download =Button(root,text="Download",command=threading.Thread(target=download).start)
download.place(x=280 ,y=220)

status = Label(root, text= "Status: Ready " ,font="calibre 10 italic" ,fg="black" , bg="white" ,anchor="w")
status.place(rely=1 ,anchor="sw" , relwidth=1)






root.mainloop()

