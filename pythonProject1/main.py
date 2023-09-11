from tkinter import *
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter.messagebox  import showinfo,showwarning
from tkinter.filedialog import askdirectory

def path():
	global add
	add=askdirectory()

def save():
	global add
	try:
		time = int(a2.get())
		addr=add+"/"+"rec1.wav"
		showinfo(title="Start",message="Recording Started")
		reco = sd.rec((time * 44100), samplerate=44100, channels=2)
		sd.wait()
		write(addr, 44100, reco)
		showinfo(title="End", message="Recording Ended")
	except:
		showwarning(title="Time",message="Wrong Format Time")

def prompt():
	global a2
	win=Tk()
	win.geometry("480x500")
	win.resizable(False,False)
	win.title("Aboli's Task 2")
	win.config(bg="indigo")

	tl = Label(win, text="Voice Recorder By Aboli", font=("Cambria ", 15), bg="Orange")
	tl.place(x=100, y=0, height=50, width=300)

	img=PhotoImage(file="mic1.png")
	a1=Label(win,image=img)
	a1.place(x=30,y=60,height=200,width=420)

	a2=Entry(win,font=(20))
	a2.place(x=250,y=280,height=50,width=200)

	a3=Label(win,text="Enter Time in Second",font=("Cambria ",15),bg="Red")
	a3.place(x=30,y=280,height=50,width=200)

	a4=Button(win,text="Select Directory",font=("Cambria ",15),command=path,bg="yellow")
	a4.place(x=30,y=350,height=50,width=420)

	a5=Button(win,text="Click Here to Start Recording",font=("Cambria ",15),command=save,bg="Green")
	a5.place(x=30,y=430,height=50,width=420)
	win.mainloop()

prompt()