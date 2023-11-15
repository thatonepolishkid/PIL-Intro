import os
from PIL import Image

folder_dir = r'C:\Users\<INSERT USER HERE>\Desktop\phone_pictures'
destination_dir = r'C:\Users\<INSERT USER HERE>\Desktop\move pictures to folder\\'

def rename_image(folder):
    for infile in os.listdir(folder):
        f, e = os.path.splitext(infile)
        outfile = f + ".JPEG"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(destination_dir + outfile)
            except OSError:
                print("cannot convert", infile)



def shape_rotate_img(folder):
    for infile in os.listdir(folder):
        im = Image.open(infile)
        im = im.resize((128, 128))
        im  = im.rotate(90)
        print(infile + "rotated, and resized!")


os.chdir(folder_dir)
rename_image(folder_dir)
os.chdir(destination_dir)
shape_rotate_img(destination_dir)
