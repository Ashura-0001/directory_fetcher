'''
This is the sole directory fetcher i have yet seen anywhere that runs and functions fully in the terminal
without any need of libraries or tkinter (it is more than a library ngl) i know this program can be made 
much simpler by turning some lists into dictionaries and stuff but i stuck with the lists and there is a 
very little bleak chance of me making this better afterall this program was just made for fun and proving\
programmes can be made much much idepentaly with simple python packages too... MWAHAHAHAHA

Also i admit that i have used some single variables in diffrent manners but that was just to
eliminate confusion and a swarm of multiple variable so please don't criticize me :>>>
'''
 
import os 
from os import system
from time import sleep


def dotanimation():
    
    max_no_of_dots = 3
    list_of_dots = ["."*i + " "*(max_no_of_dots-i) + "\r" + "Processing" for i in range (1, max_no_of_dots + 1)]
    list_of_dots.append(" "*max_no_of_dots + "\r")
    print ("Processing", end="")
    for x in range (0,3):  
        for pattern in list_of_dots:
            print (pattern, end="") 
            sleep (0.2)
def cls():
    system('cls')
def drive_listing(list):
    list.insert(0, "Terminate Process")
    print (" ")
    for x in range (0, len(list)):
        print ("[{0}]".format(x), list[x])
def folder_listing(list):
    list.insert(0, "Terminate Process")
    list.append("End path up until here only")
    print (" ")
    for x in range (0, len(list)):
        print ("[{0}]".format(x), list[x])
def list_choice(parentdir, typeofdir ):
    #need to specify typeofdir as 0 for drives, 1 for normal folders
    input_user = int(input("\n insert the index no. of option you want to choose "))
    global chosen_path
    global path_status 
    if (input_user == 0):
        terminate()
    elif (typeofdir == 0):
        chosen_path = parentdir[input_user]
        path_status = True
    elif (typeofdir == 1) and (input_user in range (1, len(parentdir)-1)):
        chosen_path = parentdir[input_user]
        path_status = True
    elif (typeofdir == 1) and (input_user == len(parentdir)-1):
        path_status = False
        chosen_path = os.getcwd()
def terminate():
    cls()
    print ("Process has been TERMINATED Succesfully !\n")
    exit()
def subdirectories_listing(chosen_dir):
    os.chdir(chosen_dir)
    global cwd
    cwd = os.getcwd()
    print ("current path is :- ", cwd)
    global sub_directories
    sub_directories = os.listdir(cwd)
    if "$RECYCLE.BIN" in sub_directories:
        sub_directories.remove("$RECYCLE.BIN")
        folder_listing(sub_directories)
    else:
        folder_listing(sub_directories)

cwd_initial = os.getcwd()
final_path = ""


drives = [chr(x) + ":\ " for x in range (65, 91) if os.path.exists(chr(x) + ":\ ")]
print ("Available drives in this computer are:- ")
drive_listing(drives)
list_choice(drives, 0)
dotanimation()
path_status = path_status
chosen_path = chosen_path

while path_status:
    cls()
    subdirectories_listing(chosen_path)
    parentdir = sub_directories
    list_choice(parentdir, 1)
    path_status = path_status
    chosen_path = chosen_path
    dotanimation()

final_path = chosen_path
cls()
print ("saved path is :- ", final_path)