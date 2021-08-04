# Program to make a simple
# login screen

from tkinter import *
import tkinter as tk
from tkinter import font as tkfont 
import os
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path



root=tk.Tk()

#
  
icon_path = os.path.abspath("Antivirus_Logo.png")
# setting the windows size
root.geometry("500x400")
#ICon
photo = PhotoImage(file = icon_path)
root.iconphoto(False, photo)

root.title("Kilo Antivirus installer")
root.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
email_var=tk.StringVar()
purchase_var=tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
	user_name=name_var.get()
	password=passw_var.get()
	email=email_var.get()
	purchase=purchase_var.get()

	name = open(username_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(user_name) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(username_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Password
	name = open(password_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(password) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(password_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Email
	name = open(email_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(email) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(email_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#purchase
	name = open(purchase_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(purchase) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(purchase_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file
	

	
# creating a label for
label9 = tk.Label(root, bg="lightpink" , text="Ki-LO Installer v1.6.0", font=("Centuary Cchoolboook L", 18), height = 4, width = 30 )
label9.place(x=11,y=0)
# name using widget Label
name_label = tk.Label(root, text = 'Username:', font=('calibre',20, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',15,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password:', font = ('calibre',20,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',15,'normal'), show = '*')

# Email
email_label = tk.Label(root, text = 'E-Mail:', font = ('calibre',20,'bold'))

# creating a entry for email
email_entry=tk.Entry(root, textvariable = email_var, font = ('calibre',15,'normal'))

# Purchase
purchase_label = tk.Label(root, text = 'Purchase Date: ', font = ('calibre',15,'bold'))

# creating a entry for email
purchase_entry=tk.Entry(root, textvariable = purchase_var, font = ('calibre',15,'normal'))



# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root, bg="yellow" , text="Sumbit", command=submit, height = 5, width = 15 )
#next


# placing the label and entry in
# the required position using grid
# method
name_label.place(x=10,y=130)
name_entry.place(x=160,y=130)
passw_label.place(x=10,y=160)
passw_entry.place(x=160,y=160)
email_label.place(x=10,y=190)
email_entry.place(x=160,y=190)
purchase_label.place(x=10,y=220)
purchase_entry.place(x=160,y=220)
sub_btn.place(x=20,y=290)




# performing an infinite loop
# for the window to display
root.mainloop()

