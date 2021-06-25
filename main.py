#all the necessary imports required in the project.
from tkinter import *
from PIL import Image,ImageTk#basically for background image.
import random
from tkinter import messagebox

#list of words
words = ['test', 'rescue', 'interfere', 'light', 'woozy', 'fetch', 'wrong', 'bruise', 'abracadabra', 'mystery', 'socialism', 'awakened', 'amazing', 'comedian', 'appreciation', 'education', 'absurd', 'GloriusPurpose', 'Assgaurd', 'RAMAN', 'Hostel', 'Python is fun', 'kudos', 'Nice Game', 'TypoSpeed', 'BigBOSS']

#defined functions
def labelslider():
    '''
    This is the function responsible for sliding the the text  : '~~~WELCOME TO TYPOSPEED~~~~' . under this first we pass an empty string , and a count variable starting with 0 
    uptil the length of passed text . Now the empty string (sliderwords) keeps on getting updated with each next character from the passed string , and this we have fixed after 
    120 microseconds , the function labelslider will be called under the fontlabel.
    '''
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
    '''
    This function is responsible for the timer of 60 seconds we have put , under the timeleft lable . We will be basically decrementing the 60 to 0 , with color change from
    green to red as it slips below 10 , as a mark of DANGER / HURRY . To make this decrementation in intervals of seconds , we call the function time under timerlabelcount 
    after 1000 ms using the after() function . 
    '''
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
        #When the timeleft becomes less than 0 . The lable consisting of the final score flashes on the screen . 
        hintlabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score - miss))
        #Along with it comes a message box , asking for a retry or cancel .
        rr = messagebox.askretrycancel('Notification', 'To try again click on Retry')
        if (rr == True):
            #If a person clicks on retry , then everything is reseted using following block of code.
            score = 0
            timeleft = 60
            miss = 0
            timerlabelcount.configure(text=time, fg='green')#Timer font color reseted back to green .
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])#The display of words also resetted.
            scorelabelcount.configure(text=score)


def startgame(event):
    '''
    This function is responsible for the running of whole game . 
    '''
    global score, miss
    if (timeleft == 60): #if timeleft is at 60 , time() function is called , which runs the timer.
        time()
    hintlabel.configure(text='')#with the starting of timer , the hintlabel's text is made an empty string so that it is out of screen.

    if (wordentry.get() == wordlabel['text']):#incrementing the score if the input string matches with any of it in the wordlist.
        score += 1
        scorelabelcount.configure(text=score)

    else:
        miss += 1#if input string is unmatched then miss is incremented .

    random.shuffle(words)#using the shuffle function from the random variables , we are calling random strings from the wordlist. 
    wordlabel.configure(text=words[0])

    wordentry.delete(0, END)#this line clears the entry widget after <return> is pressed from the keyboard.



#main window of GUI
root = Tk()#forms the main GUI window
root.wm_geometry('800x900')#defined the geometry of the main window.


#applying background image for the main GUI window.
load = Image.open(r'r.jpg')
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
