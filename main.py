from tkinter import *
import random
import time
def animate():
    mainLabel['image'] = dice3
    time.sleep(0.05)
    root.update()
    mainLabel['image'] = dice5
    time.sleep(0.05)
    root.update()
    mainLabel['image'] = dice2
    time.sleep(0.05)
    root.update()
    mainLabel['image'] = dice6
    time.sleep(0.1)
    root.update()
    mainLabel['image'] = dice4
    time.sleep(0.1)
    root.update()
    mainLabel['image'] = dice2
    time.sleep(0.1)
    root.update()
    mainLabel['image'] = dice6
    time.sleep(0.2)
    root.update()
    mainLabel['image'] = dice4
    time.sleep(0.2)
    root.update()
    mainLabel['image'] = dice1
    time.sleep(0.25)
    root.update()
    mainLabel['image'] = dice5
    time.sleep(0.28)
    root.update()
    mainLabel['image'] = dice2
def roll():
    temp = random.randint(1,6)
    animate()
    if temp == 1:
        mainLabel['image'] = dice1
        textLabel['text'] = "It's a 1!"
    elif temp == 2:
        mainLabel['image'] = dice2
        textLabel['text'] = "It's a 2!"
    elif temp == 3:
        mainLabel['image'] = dice3
        textLabel['text'] = "It's a 3!"
    elif temp == 4:
        mainLabel['image'] = dice4
        textLabel['text'] = "It's a 4!"
    elif temp == 5:
        mainLabel['image'] = dice5
        textLabel['text'] = "It's a 5!"
    else:
        mainLabel['image'] = dice6
        textLabel['text'] = "It's a 6!"
    root.update()
def reset():
    mainLabel['image'] = PhotoImage(file='images/empty.png')
    textLabel['text'] = ''
    root.update()
root = Tk()
root.resizable(0,0)
root.configure(background='#1321ba')
root.geometry('500x500+550+100')
root.title('Dice Rolling Simmulator')
root.iconbitmap('images/icon.ico')
dice1 = PhotoImage(file = 'images/1.png')
dice2 = PhotoImage(file = 'images/2.png')
dice3 = PhotoImage(file = 'images/3.png')
dice4 = PhotoImage(file = 'images/4.png')
dice5 = PhotoImage(file = 'images/5.png')
dice6 = PhotoImage(file = 'images/6.png')
frame = Frame(root,height=380,width=600,bg = "#1B1B1B")
frame.pack()
frame.place(x=0,y=150)
mainLabel = Label(frame,bg="#1B1B1B") #image and animation label
mainLabel.pack()
mainLabel.place(x = 150, y = 70)
textLabel = Label(frame,bg="#1B1B1B",font=('fixedsys',20,'bold'),fg='white') #result label
textLabel.pack()
textLabel.place(x = 170,y=280)
btn = Button(root,text='Roll the dice',command=roll,font=('times new roman',16,'bold'),bg="#991506",fg='white',relief=RAISED,width=20,height=2)
btn.pack()
btn.place(x = 130, y = 35)
resetbtn = Button(root,text='Reset',command=reset,font=('times new roman',14,'bold'),bg="#54555c",fg='white',relief=GROOVE)
resetbtn.pack()
resetbtn.place(x = 10, y = 100)
root.mainloop()