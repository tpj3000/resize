# from xml.sax.handler import property_declaration_handler

from errno import WSAENAMETOOLONG
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
folders = folders[:-2]

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
                profile = ImageCms.getOpenProfile("C:\\Windows\\System32\\spool\\drivers\\color\\eciRGB_v2.icc")
                width = im.width
                height = im.height
                print (width)
                print (height)
                if height > width:
                    ratio = (height / width)
                else:
                    ratio = (width / height)
                long_dim = 1500
                if width > height:
                    (new_width, new_height) = (long_dim, int(long_dim / ratio))
                    im_resized = im.resize((new_width, new_height))
                else:
                    im_resized = im.resize((int(long_dim / ratio), long_dim))
                    
                print (im_resized.width)
                print (im_resized.height)
        
                im_resized.save(i, format=None, icc_profile=profile.tobytes())
    
sizer()
     





    