import os
import shutil
path=input("enter a folder which u want to sort ")
lof=os.listdir(path)
for file in lof:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+"/"+file,path+'/'+ext+'/'+file)
print(lof)