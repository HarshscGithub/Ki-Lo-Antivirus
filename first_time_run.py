#Imports
from path_of_all_usr_crdn import username_file_path,password_file_path,email_file_path

#Inputs
user_name = input("Enter your usr_name: ")
password = input("Enter your password_name: ")
email = input("Enter your email_name: ")

#Username
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