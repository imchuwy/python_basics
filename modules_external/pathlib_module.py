from pathlib import Path


#Absolute Path - Start the directory from the start user
#Relative path - Starts from the directory of where we are right now

path = Path("modules_external")
print(path.exists()) #boolean of whether this exist
print(path.mkdir()) #makes a new  directory
print(path.rmdir()) #removes a directory

path = Path() #This changes to current path
for file in path.glob('*.py'): #Glob method searches in current path. for *.py files. Can do *.*
    print(file)