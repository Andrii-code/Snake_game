import tkinter
import random
import pygame
import time
pygame.init()
from tkinter import*
from PIL import ImageTk, Image
n=100000
width = 800
height = 600
segsize = 20
game = True
points = 0
speed = 300
song = pygame.mixer.Sound('fon.mp3')  # відкриває mp3.file
song.set_volume(1.0)  # регулює звук
song.play(-1)  # означає що музика гратиме безкінечн
def main():
    global game
    global Image
    global points, speed
    if game:
        s.move()
        x1, y1, x2, y2 = canvas1.coords(s.segments[-1].body)#отримуємо координати голови
        head = canvas1.coords(s.segments[-1].body)
        a2 = canvas1.coords(food)
        Points1(0)
        if x2 > 800 or x1 < 0 or y1 < 0 or y2 > 600:
            game = False
        elif a2 == head:
            canvas1.delete(food)
            Create_food()
            points += 1
            Points1(points)
            s.add_snake()
            #Speed_Change()
        for a in range(len(s.segments)-1):
            if head == canvas1.coords(s.segments[a].body):
                game = False
        root.after(speed, main)  # означає, що кожних 200 мілісекунд, запускатиметься функція main
        text1 = Label(root, text=f"SPEED {speed}", font=('Tahoma', 20), fg="yellow", bg="blue")
        text1.place(x=150, y=20)
    else:
        Game_End_Screen()
#def Speed_Change():
    #global speed
    #if points == 4:
        #speed = speed - 60
    #elif points == 8:
        #speed = speed - 20
    #elif points == 12:
        #speed = speed - 20
    #elif points == 16:
        #speed = speed - 20
    #elif points == 20:
        #speed = speed - 20
    #elif points == 24:
        #speed = speed - 20
def Start_Game():
    global s
    Create_food()
    s = Segment_Create()
    canvas1.bind("<KeyPress>", s.Change_Direction)#для управління нашої змійки; Keypress керує стрілочками
    canvas1.tag_bind(restart, "<Button-1>", click)#button-1 ліва клавіша миші, якщо ми натиснули то запускається функція click
    canvas1.tag_bind(exit1, "<Button-1>", Close)  # button-1 ліва клавіша миші, якщо ми натиснули то запускається функція close
    main()
    #Speed_Change()
    oclock_change()
def Segment_Create():
    segments = [Segment(segsize, segsize), Segment(2*segsize, segsize), Segment(3*segsize, segsize)]
    return Snake(segments)
def Close(root):
    exit()
def Status(item, state):
    canvas1.itemconfigure(item, state=state)#state червоний це параметр
    canvas1.itemconfigure(item, state=state)
def Create_food():
    global food
    pos_x = segsize*random.randint(1, 39)
    pos_y = segsize*random.randint(1, 29)
    food = canvas1.create_oval(pos_x, pos_y, pos_x+segsize, pos_y+segsize, fill="yellow")
def Game_End_Screen():
    global song
    Status(restart, "normal")#normal показує що він є на екрані, disable не дозволяє
    Status(exit1, "normal")
    song.stop()
    Destroy_Label()
def Destroy_Label():
    global text1, oclock_change
    text1.place_forget()#forget знищує
class Snake(object):#через параметр обєкт ми задаємо segments через return
    def __init__(self, segments):
        self.segments = segments
        self.dir = {"Down":(0,1),"Right":(1,0),"Up":(0,-1),"Left":(-1,0)}
        self.vector = self.dir["Right"]
    def add_snake(self):
        last_seg=canvas1.coords(self.segments[0].body)
        self.segments.insert(0, Segment(last_seg[0]-20,last_seg[1]-20))#
    def move(self):
        for a in range(len(self.segments)-1):#проходимо по змінній а, і дізнаємося довжину
            segmentall = self.segments[a].body#2 крапки вказують як шлях
            x1, y1, x2, y2 = canvas1.coords(self.segments[a+1].body)#coords - координати
            canvas1.itemconfig(self.segments[a+1].body, fill="pink")#itemconfig змінює якось елемент, в нашому випадку на біле
            canvas1.coords(segmentall, x1, y1, x2, y2)
        x1, y1, x2, y2 = canvas1.coords(self.segments[-2].body)#одержуємо координати передостаннього елементу, якщо біля цифри є мінус, то рахунок іде з кінця
        canvas1.coords(self.segments[-1].body, x1 + self.vector[0]*segsize, y1 + self.vector[1]*segsize,
                       x2 + self.vector[0]*segsize, y2 + self.vector[1]*segsize)
    def Change_Direction(self,event):#через event проходить KeyPress та метод bind
        if event.keysym in self.dir:
            self.vector = self.dir[event.keysym]
    def Snake_Delete(self):
        for segment in self.segments:
            canvas1.delete(segment.body)
class Segment(object):
    def __init__(self, x, y):
        self.body = canvas1.create_oval(x, y, x+segsize, y+segsize, fill="white")
def click(event):
    global game, points, min, sec
    game = True
    points = 0
    sec = 0
    min = 0
    s.Snake_Delete()
    canvas1.itemconfigure(restart, state='hidden')
    canvas1.itemconfigure(exit1, state='hidden')
    canvas1.delete(food)
    song.play(-1)  # означає що музика гратиме безкінечно
    Start_Game()
sec = 0
sec1 = 0
min = 0
def oclock_change():
    global sec, sec1, min
    oclock = Label(root, font=('Arial', 20), fg="black", text=f"{min}:{sec1}{sec}")
    oclock.place(x=390, y=20)
    sec += 1
    if sec == 11:
        sec = 0
        sec1 += 1
        oclock.config(text=f"{min}:{sec1}{sec}")
        if sec1 == 5:
            sec = 0
            min += 1
            oclock.config(text=f"{min}:{sec1}{sec}")
    if game:
        root.after(1000, oclock_change)
def Continue():
    global n
    n = 1
    time.sleep(n)
root = Tk()
root.title("Змійка")
root.geometry("800x600")
canvas1 = Canvas(root, width=800, height=600)
canvas1.grid()
def pause():
    global n
    time.sleep(n)#n вказує скільки треба чекати, sleep повна зупинка
def Points1(p):
    p = points
    text1 = Label(root, text=f"POINTS {p}", font=('Tahoma', 20), fg="yellow", bg="blue")
    text1.place(x=600, y=20)
button = Button(root, text="||", command=pause)
button.place(x=120, y=20)
button1 = Button(root, text="|>", command=Continue)
button1.place(x=80, y= 20)
canvas1.focus_set()
pilImage = Image.open("123.png")
Imagefon = ImageTk.PhotoImage(pilImage)
imagesprite = canvas1.create_image(0, 0, anchor=NW, image=Imagefon)#anchor вказуємо від якого кінця ставимо картинку North West
restart = canvas1.create_text(width/2, height/2, font=('Arial', 20), fill = "RED", text = "New game", state='hidden')
exit1 = canvas1.create_text(width/2, height/2-segsize, font=('Tahoma',20), fill="YELLOW", text="Exit",state='hidden')
Start_Game()
mainloop()