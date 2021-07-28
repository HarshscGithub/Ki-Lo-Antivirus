import time
from tkinter import *
import random
from all_paths import Picture_path

time = random.randint(100, 180)
percentage_c = random.randint(1, 100)



root = Tk()
root.withdraw()
root.geometry("500x600")
Label(root,text="I am main window").pack()

class SplashScreen:
    def __init__(self):

        def switch_to_pro():
            Label(self.a,text="Comming Soon to Ki-Lo Ativirus 1.5.0",font=("german", 20)).pack()

        self.a = Toplevel()
        self.a.title("Scan Utility")
        self.a.geometry("900x600")

        from all_paths import icon_path
        photo = PhotoImage(file = icon_path)
        self.a.iconphoto(False, photo)

        self.percentage = 0
        Label(self.a,text="Please wait while we are doing a quick scan.",font=("Italic", 20)).pack()
        self.load = Label(self.a,text=f"Scaning...{self.percentage}%,",font=("Italic",20))
        self.load.pack()
        self.load_bar()

        button1 = Button(self.a, bg="lightpink" , text="Switch To Pro", command=switch_to_pro, height = 5, width = 20,font=("courier"))
        button1.pack()

    def load_bar(self):
        self.percentage +=5 #Edit 5
        self.load.config(text=f"Scaning......{self.percentage}%")
        if self.percentage == 100:
            # importing required packages 
            import tkinter 
            from PIL import ImageTk, Image 
            import os 

            # creating main window 
            

            # loading the image 
            img = ImageTk.PhotoImage(Image.open(Picture_path)) 

            # reading the image 
            panel = tkinter.Label(self.a, image = img) 

            # setting the application 
            panel.place(x=70,y=300)

            # running the application 
            self.a.mainloop()


            return
        else:
            root.after(percentage_c,self.load_bar) # Edit 100
            

SplashScreen()

root.mainloop()


