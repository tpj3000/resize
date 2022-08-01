# from xml.sax.handler import property_declaration_handler

import os, shutil, glob
from pathlib import Path
from PIL import Image, ImageCms

print ('Checking current working directory', os.getcwd())

# copy all subdirectories to new working directory
src = os.getcwd()
dest = "./resized"
shutil.copytree(src, dest) 
os.chdir("./resized")


print ('Confirm current working directory has changed to resized', os.getcwd())

path = os.getcwd()

print ('Path is set to', path)

folders = os.listdir(path)
del folders[3]

print (folders)

for f in folders:
     os.chdir(os.path.join(path + "/" + f))
     print (os.getcwd())
     
     filelist = os.listdir()
     print (filelist)
     
     def sizer():
        for i in glob.glob("*.jpg"):
            print (i)
            with Image.open(i) as im:
                width = im.width
                height = im.height
                print (width)
                print (height)
                ratio = (width / height)
                if width > height:
                    new_height = 1500
                    (new_width, new_height) = (int(ratio * new_height), new_height)
                    im_resized = im.resize((new_width, new_height))
                else:
                    im_resized = im.resize((new_height, int(ratio * new_height)))
                    
                print (im_resized.width)
                print (im_resized.height)
                im_resized.save(i, format=None)
        return
        
     sizer()
     
     # save with color profile, else for portrait images 
     





    