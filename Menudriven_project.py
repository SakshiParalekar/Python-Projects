import os
print("1.Create a directory\n2.Remove a directory\n3.Rename a directory\n4.Delete a directory\n5.Display a present working directory")

choice=int(input("Enter Your Choice:"))
if choice==1:
    name=str(input("Enter the name of the directory:"))
    os.mkdir(name)

if choice==2:
    name=str(input("Enter the name of the directory:"))
    os.rmdir(name)
    
if choice==3:
    os.rename("dir1","Directory1")
    
if choice==4:
    os.remove("C:/Users/SAKSHI/Directory1")
    
if choice==5:
    print("File location using os.getcwd():",os.getcwd())
    
