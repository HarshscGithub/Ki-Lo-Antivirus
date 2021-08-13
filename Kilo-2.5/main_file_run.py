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
from all_paths import icon_path
from all_paths import Picture_path

#
import random
time = random.randint(100, 180)
percentage_c = random.randint(1, 100)
#Link
import webbrowser
def callback(url):
    webbrowser.open_new(url)

#Import path
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path

#Import file
with open(purchase_file_path, 'r') as file:
    pur_date = file.read().rstrip('\n')

with open(username_file_path, 'r') as file:
    username = file.read().rstrip('\n')

with open(password_file_path, 'r') as file:
    password = file.read().rstrip('\n')

with open(email_file_path, 'r') as file:
    email = file.read().rstrip('\n')

class Kilo_Antivirus(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

         #Icon
        photo = PhotoImage(file = icon_path)
        self.iconphoto(False, photo)

        self.title("Kilo 2.0 Antivirus")
        self.title_font = tkfont.Font(family='Cursive', size=18, weight="bold", slant="italic")

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
        for F in (Feedback, Home, Scan, User_info, Info, Scan_Utility):
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


class User_info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.user_name = StringVar()

	

        self.controller = controller
        label = tk.Label(self, text="Central", font=("Brush Script Std", 14))
        label.place(x=400,y=0)


        label2 = tk.Label(self, text="User Name", font=("Arial Bold", 14))
        label2.place(x=230,y=30)

        v = StringVar(self, value=username)
        E1 = Entry(self, bd =5, textvariable=v)
        E1.place(x=380,y=30)


        label3 = tk.Label(self, text="Password", font=("Arial Bold", 14))
        label3.place(x=230,y=80)

        a = StringVar(self, value=password)
        E2 = Entry(self, bd =5, textvariable=a)
        E2.place(x=380,y=80)

        label4 = tk.Label(self, text="D-O-B", font=("Arial Bold", 14))
        label4.place(x=230,y=130)

        E3 = Entry(self, bd =5)
        E3.place(x=380,y=130)

        label5 = tk.Label(self, text="Email", font=("Arial Bold", 14))
        label5.place(x=230,y=180)

        ab = StringVar(self, value=email)
        E4 = Entry(self, bd =5, textvariable=ab)
        E4.place(x=380,y=180)

        label6 = tk.Label(self, text="Remaining Days", font=("Arial Bold", 14))
        label6.place(x=230,y=230)
        #Date
        import datetime 
        from datetime import date  
        date_time_obj = datetime.datetime.strptime(pur_date, '%d-%m-%Y').date()
        main_date = date_time_obj + datetime.timedelta(days=365)
        
        remaining_days = (main_date - date.today()).days
      
              
       	
        Total_days = "365" + " " + "days"
	#remaining_days = str(remaining_days) + "days"

        label5 = tk.Label(self, text=remaining_days, font=("Italic", 14))
        label5.place(x=385,y=230)
	
        label88 = tk.Label(self, bg="orange" , text=str(date.today()), height = 6, width = 20 )
        label88.place(x=200,y=400)	

        label7 = tk.Label(self, text="Subscription", font=("Arial Bold", 14))
        label7.place(x=230,y=280)

        label8 = tk.Label(self, text=Total_days, font=("Italic", 14))
        label8.place(x=380,y=280)

        label9 = tk.Label(self, bg="lightblue" , text="Version 2.0.0", height = 6, width = 30 )
        label9.place(x=370,y=400)
	
	
	

        #label2.pack()

        
        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button8 = tk.Button(self, bg="lightpink" , text="User Info", command=lambda: controller.show_frame("User_info"), height = 4, width = 25 )
	
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=5,y=10)
        button2.place(x=5,y=105)
        button3.place(x=5,y=205)
        button7.place(x=5,y=305) 
        button8.place(x=5,y=405)

class Scan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))

        

        button4 = tk.Button(self, bg="lightblue" , text="Quick Scan", command=lambda: controller.show_frame("Scan_Utility"), height = 4, width = 20 )
                            
        button5 = tk.Button(self, bg="lightblue" , text="Full Scan", command=lambda: controller.show_frame("Scan_Utility"), height = 4, width = 20 )

        button6 = tk.Button(self, bg="lightblue" , text="Custom Scan", command=lambda: controller.show_frame("Scan_Utility"), height = 4, width = 20 )
        
        
        button4.place(x=150,y=100)
        button5.place(x=350,y=100)
        button6.place(x=240,y=210)
        


      
        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="lightpink" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 25 )
        
        button8 = tk.Button(self, bg="yellow" , text="User Info", command=lambda: controller.show_frame("User_info"), height = 4, width = 15 )
	
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=5,y=10)
        button2.place(x=5,y=105)
        button3.place(x=5,y=205)
        button7.place(x=5,y=305) 
        button8.place(x=5,y=405)


        button.pack()

        


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_head = tk.Label(self, bg="Pink" , text="Kilo 2.0.0 Antvirus", font=("Courier", 14), height = 2, width = 53 )
        label2 = tk.Label(self, bg="CYAN" , text="Home", font=("Courier", 14), height = 2, width = 13 )   
     
        button2 = tk.Button(self, bg="lightgreen" , text="Update", height = 5, width = 25 )

        button3 = tk.Button(self, bg="lightyellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 25 )

        button7 = tk.Button(self, bg="lightpink" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 25 )
        
        button8 = tk.Button(self, bg="lightblue" , text="Kilo 2.0 Central", command=lambda: controller.show_frame("User_info"), height = 12, width = 25 )

        button9 = tk.Button(self, bg="lightblue" , text="feedback", command=lambda: controller.show_frame("Feedback"), height = 5, width = 25 )
	
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))

        label89 = tk.Label(self, bg="orange" , text=str(date.today()), height = 5, width = 25)
        label90 = tk.Label(self, bg="Lightblue" , text="Made by Harsh Chaudari", height = 5, width = 25)
        label89.place(x= 1, y=330)
        label90.place(x=400 ,y =330)
        label2.place(x=220,y=60)
        label_head.place(x=5,y=10)
        button2.place(x=205,y=115)
        button3.place(x=205,y=210)
        button7.place(x=405,y=115)
        #label88.place(x=405,y=210)
        button9.place(x=405,y=210)
          
        button8.place(x=5,y=115)
        
        
        

class Scan_Utility(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan Utility", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))

        def switch_to_pro():
            Label(self,text="Comming Soon to Ki-Lo Ativirus 2.5.0",font=("german", 20)).pack()

        def start_scan():  
            def switch_to_pro():
                Label(self,text="Comming Soon to Ki-Lo Ativirus 2.5.0",font=("german", 20)).pack()

            self.percentage = 0
            Label(self,text="Please wait while we are doing a quick scan.",font=("Italic", 15)).pack()
            self.load = Label(self,text=f"Scaning...{self.percentage}%,",font=("Italic",15))
            self.load.pack()
            self.load_bar()

       

        start_btn = tk.Button(self, bg="lightblue" , text="Start Scaning!", command=start_scan, height = 4, width = 20 )
        start_btn.pack()

        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", height = 5, width = 15 )

        button3 = tk.Button(self, bg="yellow" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 15 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button8 = tk.Button(self, bg="yellow" , text="User Info", command=lambda: controller.show_frame("User_info"), height = 4, width = 15 )
	
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=5,y=10)
        button2.place(x=5,y=105)
        button3.place(x=5,y=205)
        button7.place(x=5,y=305) 
        button8.place(x=5,y=405)

    def load_bar(self):
        self.percentage +=2 #Edit 5
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
            panel = tkinter.Label(self, image = img) 

            # setting the application 
            panel.place(x=170,y=200)

            # running the application 
            self.mainloop()


            return
        else:
            self.after(percentage_c,self.load_bar)  # Edit 100
         
                            

        

        
class Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="About", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=" Home Page ",
                           command=lambda: controller.show_frame("Home"))
        
        about = tk.Label(self, bg="lightGreen" , text="No-Copyright (C) 2021 harshsc2007 Ki-Lo - All Rights Reserved\nYou may use, distribute and modify this code,\nYou should write name  harshsc2007 GITHUB in source code.\nif your using your own then no need of putting my name,but\nif your doing publicity of my code modifed then you put my my name", height = 10, width = 56 )
        about.place(x=140,y=90)
        
        history = tk.Label(self, bg="coral" , text="Release History of Kilo 2.0.0\n\nKilo 2.0 main release :4-08-2021 \nKilo 2.0 Pre-Build 2 : 1-08-2021\nKilo 2.0 Pre-Build 1 : 30-07-2021", font=("Courier", 13) ,height = 8, width = 38 )
        history.place(x=140,y=290)

        button1 = tk.Button(self, bg="yellow" , text="Home", command=lambda: controller.show_frame("Home"), height = 5, width = 15 )
                            
        button2 = tk.Button(self, bg="yellow" , text="Update", height = 5, width = 15 )

        button3 = tk.Button(self, bg="lightpink" , text="About", command=lambda: controller.show_frame("Info"), height = 5, width = 25 )

        button7 = tk.Button(self, bg="yellow" , text="Scan", command=lambda: controller.show_frame("Scan"), height = 5, width = 15 )
        
        button8 = tk.Button(self, bg="yellow" , text="User Info", command=lambda: controller.show_frame("User_info"), height = 4, width = 15 )
	
        button2.bind("<Button-1>", lambda e: callback("https://github.com/harshsc2007/Kilo-Antivirus/releases"))
        button1.place(x=5,y=10)
        button2.place(x=5,y=105)
        button3.place(x=5,y=205)
        button7.place(x=5,y=305) 
        button8.place(x=5,y=405)


        button.pack()

class Feedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Feed Back", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        #String
        ab = StringVar(self, value="")
        feedback = Entry(self,textvariable=ab)
        feedback.place(x=20,y=40)
        feedback.place(height=340, width=560)
        #Sumbit Button
        def submit():
            import smtplib, ssl

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "harshantivirus2@gmail.com"  # Enter your address
            receiver_email = email  # Enter receiver address
            password = "@Harsh2007"
            SUBJECT = "FeedBack from" +" "+ email
            message = 'Subject: {}\n\n{}'.format(SUBJECT, feedback.get())
            from tkinter import messagebox
            messagebox.showinfo("showinfo", "FeedBack Send succesfully")
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)


        sumbit_btn = tk.Button(self, bg="yellow" , text="Send Feedback", command= submit, height = 4, width = 20 )
        sumbit_btn.place(x=20,y= 400)
        
        
        


if __name__ == "__main__":
    app = Kilo_Antivirus()
    app.mainloop()