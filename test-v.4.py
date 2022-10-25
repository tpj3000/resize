import os, shutil, glob
from PIL import Image
from pathlib import Path

print ("Checking working Directory, ", os.getcwd())
print ("Copying files and folders to ./resized/, please wait . . .")
src = os.getcwd()
dest = "./resized"
shutil.copytree(src, dest) 
os.chdir("./resized")

print ("Confirming current directory is, ", os.getcwd())

path = os.getcwd() + "/**/**/*.jpg"

for f in glob.glob(path, recursive=True):
    print (f)

def sizer():
    for f in glob.glob(path, recursive=True):
        with Image.open(f) as im:
            width = im.width
            height = im.height
            print("Original width is: ", width)
            print("Original height is: ", height)
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
            print("Resized width is: " , new_width)
            print("Resized height is: " , new_height)
            print("Saving . . .")
            im_resized.save(f, format=None)
sizer()

