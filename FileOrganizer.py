import os
import shutil

path = input("Enter Name Of A Folder : ")
listFiles = os.listdir(path)
for file in listFiles :
    name,ext = os.path.splitext(file)
    myext = ext[1:]
    if myext=='':
        continue
# This will move the file to the directory where the name 'ext' already exists
    if os.path.exists(path+'/'+myext):
        shutil.move(path+'/'+file   , path+'/'+myext+'/'+file)
    else :
        os.makedirs(path+'/'+myext)
        shutil.move(path+'/'+file, path+'/'+myext+'/'+file)