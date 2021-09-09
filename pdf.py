"""
from fpdf import FPDF
import os
import glob

os.chdir("C:\\Users\\ynkar\\Downloads\\PHYS115_HW1")
imagelist = glob.glob("*.jpg")

pdf = FPDF()
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")
"""

# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

import os

os.chdir("C:\\Users\\ynkar\\Downloads\\...") # filepath here
# TODO write with methods for cleaner, better code

from PIL import Image

im1 = Image.open("1.jpg")
im2 = Image.open("2.jpg")
im3 = Image.open("3.jpg")
im4 = Image.open("4.jpg")

im_list = [im2,im3, im4]

pdf1_filename = "test2.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
