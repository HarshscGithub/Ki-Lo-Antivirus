import socket

computer_name = socket.gethostname()

if computer_name == "Harshs-MacBook-Pro.local" :
    path = "/Users/harshschaudhari/Desktop/Dashing_Antivirus/No_Virus_Found.png"
    print("Your computer is same.")

else:
    input_path = input("Please give path of No_Virus_Found.png:: ")
    name = open("ao_path.py", "w+") #opens file usernames.txt and gets ready to write to it
    name.write(input_path) #writes contents in file to usernames.txt
    name.close() #closes file


