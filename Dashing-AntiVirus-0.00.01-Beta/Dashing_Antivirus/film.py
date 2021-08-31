name = open("usernames.txt", "w") #opens file usernames.txt and gets ready to write to it
file = input("please type some text: ") #asks user for text in code

name.write(file) #writes contents in file to usernames.txt
name.close() #closes file
open1 = open("usernames.txt", "r") #opens file to read it
print (open1.read()) #prints whatever is in the text file