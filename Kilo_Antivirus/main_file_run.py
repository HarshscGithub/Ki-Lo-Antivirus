try:
    from datetime import date
    from tkinter import *
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    from datetime import date
    from Tkinter import *
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
#Import Variable
from path_icon import icon_path
#Link
import webbrowser
def callback(url):
    webbrowser.open_new(url)

class Kilo_Antivirus(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

         #Icon
        photo = PhotoImage(file = icon_path)
        self.iconphoto(False, photo)

        self.title("Dashing + Kilo Antivirus")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, minsize=500, weight=1)
        container.grid_columnconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(1, weight=1)


        self.frames = {}
        for F in (Home, Scan, Update, Info):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.user_name = StringVar()

        self.controller = controller
        label = tk.Label(self, text="HOME", font=("Brush Script Std", 14))
        label.place(x=200,y=0)


        label2 = tk.Label(self, text="User Name", font=("Arial Bold", 14))
        label2.place(x=30,y=30)

        v = StringVar(self, value='harshsc2007')
        E1 = Entry(self, bd =5, textvariable=v)
        E1.place(x=180,y=30)


        label3 = tk.Label(self, text="Password", font=("Arial Bold", 14))
        label3.place(x=30,y=80)

        a = StringVar(self, value='Harsh123')
        E2 = Entry(self, bd =5, textvariable=a)
        E2.place(x=180,y=80)

        label4 = tk.Label(self, text="D-O-B", font=("Arial Bold", 14))
        label4.place(x=30,y=130)

        E3 = Entry(self, bd =5)
        E3.place(x=180,y=130)

        label5 = tk.Label(self, text="Email", font=("Arial Bold", 14))
        label5.place(x=30,y=180)

        E4 = Entry(self, bd =5)
        E4.place(x=180,y=180)

        label6 = tk.Label(self, text="Remaining Days", font=("Arial Bold", 14))
        label6.place(x=30,y=230)
        #Date
        import datetime 
        from datetime import date
        
        delta = (date.today() - datetime.date(2021, 3, 19))
        remaining_days = (datetime.date(2022, 3, 19) - date.today())
      
                
       
        Total_days = "365" + " " + "days"

        label5 = tk.Label(self, text=remaining_days, font=("Italic", 14))
        label5.place(x=185,y=230)

        label7 = tk.Label(self, text="Subscription", font=("Arial Bold", 14))
        label7.place(x=30,y=280)

        label8 = tk.Label(self, text=Total_days, font=("Italic", 14))
        label8.place(x=180,y=280)

        label9 = tk.Label(self, bg="Green" , text="Version 0.9.7 ", height = 6, width = 30 )
        label9.place(x=370,y=0)

        #label2.pack()

        
        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=9,y=400)
        button2.place(x=159,y=400)
        button3.place(x=319,y=400)
        button7.place(x=479,y=400)

class Scan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))

        import importlib
        
        def Quick_scan():
            import scan
            importlib.reload(scan)
        def Full_scan():
            import scan
            importlib.reload(scan)
        def Custom_scan():
            label_4 = tk.Label(self, text="Custom Scan.\nDevelopment is in progress.", font=controller.title_font)
            label_4.pack(side="left", fill="x", pady=10)

        button4 = tk.Button(self, bg="lightblue" , text="Quick Scan", command=Quick_scan, height = 4, width = 20 )
                            
        button5 = tk.Button(self, bg="lightblue" , text="Full Scan", command=Full_scan, height = 4, width = 20 )

        button6 = tk.Button(self, bg="lightblue" , text="Custom Scan", command=Custom_scan, height = 4, width = 20 )
        
        
        button4.place(x=20,y=90)
        button5.place(x=220,y=90)
        button6.place(x=420,y=90)
        #


      
        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update" , height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=9,y=400)
        button2.place(x=159,y=400)
        button3.place(x=319,y=400)
        button7.place(x=479,y=400)


        button.pack()

        


class Update(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Update page.\nDevelopment is in progress.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))


        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update" , height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=9,y=400)
        button2.place(x=159,y=400)
        button3.place(x=319,y=400)
        button7.place(x=479,y=400)
        
        button.pack()
class Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="About", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))
        
        about = tk.Label(self, bg="lightGreen" , text="Copyright (C) 2021 harshsc2007 Ki-Lo - All Rights Reserved\nYou may use, distribute and modify this code,\nYou should write name  harshsc2007 GITHUB in source code.\nif your using your own then no need of putting my name,but\nif your doing publicity of my code modifed then you put my my name", height = 10, width = 56 )
        about.place(x=100,y=150)

        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update" , height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=9,y=400)
        button2.place(x=159,y=400)
        button3.place(x=319,y=400)
        button7.place(x=479,y=400)


        button.pack()


if __name__ == "__main__":
    app = Kilo_Antivirus()
    app.mainloop()