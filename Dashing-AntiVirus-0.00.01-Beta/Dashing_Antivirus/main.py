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

class Dashing_AntiVirus(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Dashing Antivirus")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.grid_rowconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(1, weight=1)


        self.frames = {}
        for F in (User_info, Scan, Update, Info):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("User_info")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class User_info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.user_name = StringVar()

        self.controller = controller
        label = tk.Label(self, text="USER INFO", font=("Italic Bold", 25))
        label.place(x=200,y=0)

        label2 = tk.Label(self, text="User Name", font=("Arial Bold", 20))
        label2.place(x=30,y=30)

        v = StringVar(self, value='nirajvc2001')
        E1 = Entry(self, bd =5, textvariable=v)
        E1.place(x=180,y=30)


        label3 = tk.Label(self, text="Password", font=("Arial Bold", 20))
        label3.place(x=30,y=80)

        a = StringVar(self, value='Niraj123')
        E2 = Entry(self, bd =5, textvariable=a)
        E2.place(x=180,y=80)

        label4 = tk.Label(self, text="DOB", font=("Arial Bold", 20))
        label4.place(x=30,y=130)

        E3 = Entry(self, bd =5)
        E3.place(x=180,y=130)

        label5 = tk.Label(self, text="Email", font=("Arial Bold", 20))
        label5.place(x=30,y=180)

        E4 = Entry(self, bd =5)
        E4.place(x=180,y=180)

        label6 = tk.Label(self, text="Remainig Days", font=("Arial Bold", 20))
        label6.place(x=30,y=230)

        import datetime

        delta = datetime.datetime(2020, 5, 5) - datetime.datetime.now()

       
        Total_days = "365" + " " + "days"

        label5 = tk.Label(self, text=delta, font=("Italic", 20))
        label5.place(x=180,y=230)

        label7 = tk.Label(self, text="Subscription", font=("Arial Bold", 20))
        label7.place(x=30,y=280)

        label8 = tk.Label(self, text=Total_days, font=("Italic", 20))
        label8.place(x=180,y=280)

        label9 = tk.Label(self, text="Version 0.1 Beta", font=("Italic", 10))
        label9.place(x=250,y=350)

        #label2.pack()


        button1 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 20 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", command=lambda: controller.show_frame("Update"), height = 5, width = 20 )

        button3 = tk.Button(self, bg="yellow" , text="Info", command=lambda: controller.show_frame("Info"), height = 5, width = 20 )

        
        button1.place(x=0,y=515)
        button2.place(x=200,y=515)
        button3.place(x=400,y=515)


class Scan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to User Info",
                           command=lambda: controller.show_frame("User_info"))

        def Quick_scan():
            import scan

        def Full_scan():
            import scan
        
        def Custom_scan():
            import scan


        button4 = tk.Button(self, bg="yellow" , text="Quick Scan", command=Quick_scan, height = 5, width = 20 )
                            
        button5 = tk.Button(self, bg="yellow" , text="Full Scan", command=Full_scan, height = 5, width = 20 )

        button6 = tk.Button(self, bg="yellow" , text="Custom Scan", command=Custom_scan, height = 5, width = 20 )
        
        
        button4.place(x=0,y=70)
        button5.place(x=200,y=70)
        button6.place(x=400,y=70)
        #


        button1 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 20 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", command=lambda: controller.show_frame("Update"), height = 5, width = 20 )

        button3 = tk.Button(self, bg="yellow" , text="Info", command=lambda: controller.show_frame("Info"), height = 5, width = 20 )

        
        button1.place(x=0,y=515)
        button2.place(x=200,y=515)
        button3.place(x=400,y=515)


        button.pack()

        


class Update(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("User_info"))

        button1 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 20 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", command=lambda: controller.show_frame("Update"), height = 5, width = 20 )

        button3 = tk.Button(self, bg="yellow" , text="Info", command=lambda: controller.show_frame("Info"), height = 5, width = 20 )

        
        button1.place(x=0,y=515)
        button2.place(x=200,y=515)
        button3.place(x=400,y=515)


        button.pack()

class Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("User_info"))
        
        button1 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 20 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", command=lambda: controller.show_frame("Update"), height = 5, width = 20 )

        button3 = tk.Button(self, bg="yellow" , text="Info", command=lambda: controller.show_frame("Info"), height = 5, width = 20 )

        
        button1.place(x=0,y=515)
        button2.place(x=200,y=515)
        button3.place(x=400,y=515)


        button.pack()


if __name__ == "__main__":
    app = Dashing_AntiVirus()
    app.mainloop()