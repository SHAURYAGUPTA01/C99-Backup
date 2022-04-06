import shutil
import os

s = input("enter a source folder : ")
d= input("enter a destination folder : ")

s = s+'/'
d = d+'/'

filelist=os.listdir(s)
for file in filelist:
    shutil.copy((s+file),d)