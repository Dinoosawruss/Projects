# Bulk Rename
import os
import sys

print("""Welcome to the bulk rename tool
--------------------------------
WARNING: This tool can be highly
         destructive if used
         incorrectly.
--------------------------------
Instructions:
1) Create a folder called \"Rename\"
2) Go to that folder and find the filepath
3) Put all files you wish to be reanmed
   in your rename folder
4) Run press [ENTER] key
5) Insert information asked
6) Watch as all your files are renamed
7) Ensure everything worked correctly
--------------------------------
Note:
The creators of this program will
take no responsibility for any damages
it may cause by incorrect usage and
we will offer no support. You are using
this program at your own risk.""")
run = False
while not run:
        
    cont = False

    while cont == False:
        path = input("--------------------------------\nRename File Path:\n ")

        if "RENAME" not in path.upper():
            print("--------------------------------\nSorry, that is not a rename file path\nPlease try again")
            cont = False
            
        else:
            cont = True

    if path[len(path)-1] != "/":
        path = path + "/"

    newName = input("--------------------------------\nRename to:\n ")
    fileType = input("--------------------------------\nFile Type:\n ")
    if len(fileType) > 0: 
        if fileType[0] != ".":
            fileType = "." + fileType
        
    i = 0
    try:
        for filename in os.listdir(path): 
            dst = newName + str(i) + fileType
            src = path + filename 
            dst = path + dst 
            
            os.rename(src, dst) 
            i += 1

    except FileNotFoundError:
        print("--------------------------------\nThat file could not be found")

    else:
        run = True
            
