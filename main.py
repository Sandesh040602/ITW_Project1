#list of words
words = ['test', 'rescue', 'interfere', 'light', 'woozy', 'fetch', 'wrong', 'bruise', 'abracadabra', 'mystery', 'socialism', 'awakened', 'amazing', 'comedian', 'appreciation', 'education', 'absurd', 'GloriusPurpose', 'Assgaurd', 'RAMAN', 'Hostel', 'Python is fun', 'kudos', 'Nice Game', 'TypoSpeed', 'BigBOSS']

#defined functions
def labelslider():
    global count, sliderwords
    text = '~~~WELCOME TO TYPOSPEED~~~~'

    if (count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(120, labelslider)


def time():
    global timeleft, score, miss
    if (timeleft >= 11):
        pass
    else:
        timerlabelcount.configure(fg='red')
    if (timeleft > 0):
        timeleft -= 1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000, time)
    else:
        hintlabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score - miss))
        rr = messagebox.askretrycancel('Notification', 'To try again click on Retry')
        if (rr == True):

            score = 0
            timeleft = 60
            miss = 0
            timerlabelcount.configure(text=time, fg='green')
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)


def startgame(event):
    global score, miss
    if (timeleft == 60):
        time()
    hintlabel.configure(text='')

    if (wordentry.get() == wordlabel['text']):
        score += 1
        scorelabelcount.configure(text=score)

    else:
        miss += 1

    random.shuffle(words)
    wordlabel.configure(text=words[0])

    wordentry.delete(0, END)

#imports
from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox

#main window of GUI
root = Tk()
root.wm_geometry('800x900')



load = Image.open(r'C:\Users\sanka\Desktop\r.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)


img.place(x=0,y=0)
root.title('Typospeed')
root.iconbitmap('icon.ico')
#root.configure(bg="midnight blue")

#bg = PhotoImage(file="bg2.jpg")
#my_label = Label(image=bg)
#my_label.place(x=0, y=0, relwidth=1, relheight=1)

#assigned variables values
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0


####labels

img2 = PhotoImage(file = r'C:\Users\sanka\Desktop\new.png')
l1 = Label(root,image = img2,bg='SkyBlue1')
l1.place(x=40,y=40)

fontlabel = Label(root, text='', font=('Arial Black', 25, 'bold'), bg='SkyBlue1', fg='black', width=31,justify='center')
fontlabel.place(x=31, y=110)
labelslider()

random.shuffle(words)
wordlabel = Label(root, text=words[0], font=('Bahnschrift', 30),justify='center',bg='SkyBlue1')
wordlabel.place(x=400, y=340,anchor = CENTER)

scorelabel = Label(root, text='YOUR SCORE', font=('Comic Sans MS', 20, 'bold'), bg='LightSkyBlue1')
scorelabel.place(x=60, y=200)

scorelabelcount = Label(root, text=score, font=('arial', 18, 'bold'))
scorelabelcount.place(x=140, y=255)

timerlabel = Label(root, text='TIME LEFT', font=('Comic Sans MS', 20, 'bold'), bg='LightSkyBlue1')
timerlabel.place(x=520, y=200)

timerlabelcount = Label(root, text=timeleft, font=('arial', 18, 'bold'),fg='green')
timerlabelcount.place(x=580, y=255)

hintlabel = Label(root, text='Type Word And Hit Enter Button', font=('arial', 30, 'italic bold'), bg='powder blue',
                  fg='dark grey')
hintlabel.place(x=120, y=500)

wordentry = Entry(root, font=('MS UI Gothic', 25, 'bold'), bd=10, justify='center')
wordentry.place(x=220, y=380)
wordentry.focus_set()

root.bind('<Return>', startgame)
root.mainloop()
