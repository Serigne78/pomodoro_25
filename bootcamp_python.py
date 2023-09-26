from tkinter import *
import pygame
from PIL import Image, ImageTk
import time
import math
reps = 0
FONT_NAME ="Arial"

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("time song.mp3")
    #Gerer le son 
    #Réglez le volume (0.0 - 1.0, où 0.0 est le volume le plus bas et 1.0 est le volume le plus fort)
    pygame.mixer.music.set_volume(0.5)  # Par exemple, réglez le volume à 50%

    #pygame.mixer.music.play()
    pygame.mixer.music.play()

def start_timer():
    global reps
    reps+=1
    travail = 25*60
    short_break = 5*60

    
    
    if reps % 2 ==0:
        count_down(short_break)
        canvas.itemconfig(timer_text,text="Break")   
    else:
        count_down(travail)
        canvas.itemconfig(timer_text,text="Work")   
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count %60
    if count_sec == 0 or count_sec==1 or count_sec==2 or count_sec==3 or count_sec==4 or count_sec==5 or count_sec==6 or count_sec==7 or count_sec==8 or count_sec==9:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
       
def app_and_song():
    start_timer()
    play_song()

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")



#Affichage
window = Tk()
window.minsize(700,645)
canvas = Canvas(width=700, height=645)


backround = PhotoImage(file="backround_pomodoro.png")
canvas.create_image(350, 325, image=backround)
timer_text = canvas.create_text(350, 390, text="00:00", font=("Times", "24", "bold italic"), fill="white")
canvas.create_text(350, 50, text="Pomodoro 25/5 3HOUR", font=("Times", "24", "bold italic"), fill="green")

canvas.create_text
canvas.grid(column=1 ,row=1)





#Button 
play_button = Button(text="Start", command=app_and_song, relief="ridge")
play_button.grid(column=3, row=1)
reset_button = Button(text="Reset", relief="ridge",command=reset_timer)
reset_button.grid(column=3, row=2)


window.mainloop()






