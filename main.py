# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox

words = ['test', 'rescue', 'interfere', 'light', 'woozy', 'fetch', 'wrong', 'bruise', 'abracadabra', 'mystery', 'socialism', 'awakened', 'amazing', 'comedian', 'appreciation', 'education', 'absurd', 'GloriusPurpose', 'Assgaurd', 'RAMAN', 'Hostel', 'Python is fun', 'kudos', 'Nice Game', 'TypoSpeed', 'BigBOSS']


def labelslider():
    global count, sliderwords
    text = '~QUALITY TIME WITH KEYBOARD~'
    if (count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(100, labelslider)


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




root = Tk()
root.wm_geometry('800x600')
load = Image.open(r'C:\Users\sanka\Desktop\r.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

root.title('typing speed increaser Game ')
root.iconbitmap('icon.ico')
# we have not changed the icon of the app
root.iconbitmap('Letter-T-icon_34797.ico')
root.configure(bg="midnight blue")

#bg = PhotoImage(file="bg2.jpg")
#my_label = Label(image=bg)
#my_label.place(x=0, y=0, relwidth=1, relheight=1)
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0

fontlabel = Label(root, text='', font=('Arial Black', 25, 'bold'), bg='midnight blue', fg='white', width=35)
fontlabel.place(x=10, y=10)
labelslider()

random.shuffle(words)
wordlabel = Label(root, text=words[0], font=('Bahnschrift', 40), bg='white')
wordlabel.place(x=340, y=200)

scorelabel = Label(root, text='YOUR SCORE', font=('Comic Sans MS', 25, 'bold'), bg='white', fg='black')
scorelabel.place(x=10, y=100)

scorelabelcount = Label(root, text=score, font=('arial', 25, 'bold'), bg='black', fg='white')
scorelabelcount.place(x=80, y=180)

timerlabel = Label(root, text='TIME LEFT', font=('Comic Sans MS', 25, 'bold'), bg='white', fg='black')
timerlabel.place(x=600, y=100)

timerlabelcount = Label(root, text=timeleft, font=('arial', 25, 'bold'), bg='black', fg='white')
timerlabelcount.place(x=680, y=180)

hintlabel = Label(root, text='Type Word And Hit Enter Button', font=('arial', 30, 'italic bold'), bg='powder blue',
                  fg='dark grey')
hintlabel.place(x=120, y=450)

wordentry = Entry(root, font=('MS UI Gothic', 25, 'bold'), bd=10, justify='center')
wordentry.place(x=240, y=300)
wordentry.focus_set()

root.bind('<Return>', startgame)
root.mainloop()
