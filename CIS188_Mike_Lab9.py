#CIS188_Mike_Lab9.py
from pathlib import Path
import zipfile, os
import re
import time


'''In this lab you have been given a zip file, called files.zip (attached), containing several subdirectories and within each subdirectory is a PDF and an image file.   
'''
def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

# Your task is to write a script that will move all the PDF files into a directory called PDF and the images into a directory called images. 
#counts 
countJPG = 0
countPDF = 0
# Open Zip
p = Path.home()
# Use ext for your path
ext = 'your_path' 
exampleZip = zipfile.ZipFile(p /  ext  /'files.zip')
#print(exampleZip.namelist())
exampleZip.extractall(p / ext /'workingfiles/') # makedirs not needed, extract does this for free
exampleZip.close()

# put in a sleep because zip was faster than my disk and would cause not found errors
time.sleep(5)
# Your script should create the top level folders (images and pdf), 
os.chdir('workingfiles')
os.makedirs('new/images')
os.makedirs('new/pdf')
files = p / ext /'workingfiles/files/'
cwd = p / ext /'workingfiles/new'
# move all the files 
os.chdir(files)
# Went with re because It makes more sense and glob was returning empty lists instead of objects
pdfs =  re.compile(r'^.*\.(pdf)$')
jpgs =  re.compile(r'^.*\.(jpg)$')

for filename in os.listdir(files): # parent Dir
    for image in os.listdir(filename): # Named sub directory
        mo = pdfs.search(image)
        jo = jpgs.search(image)
        if(mo is not None):
            #print(mo.group())
            countPDF += 1
            os.rename(files/filename/image, cwd/'pdf'/image )
        if(jo is not None):
            #print(jo.group())
            countJPG += 1
            os.rename(files/filename/image, cwd/'images'/image )     

time.sleep(5)

# and then print out a directory listing of both the images and pdf folders.  
pdflist = os.listdir(cwd / 'pdf')
jpglist = os.listdir(cwd / 'images')
pdfstr = 'PDFs: '
jpgstr = 'JPGs: '
for image in pdflist:
    pdfstr += " " + image
for image in jpglist:
    jpgstr += " " + image
print(pdfstr + '\n') 
print(jpgstr + '\n') 

# Finally it should print the total number of files in both of these folders.
print("Total number of jpgs in images directory :",countJPG)
print("Total number of pdfs in pdf directory :",countPDF)
# Zip up new folders

src_path = cwd
archive_name = 'new.zip'
archive_path = os.path.join(p, ext, archive_name)

with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive_file:
    for dirpath, dirnames, filenames in os.walk(src_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            archive_file_path = os.path.relpath(file_path, src_path)
            archive_file.write(file_path, archive_file_path)

with zipfile.ZipFile(archive_path, 'r') as archive_file:
    bad_file = zipfile.ZipFile.testzip(archive_file)

    if bad_file:
        raise zipfile.BadZipFile(
            'CRC check failed for {} with file {}'.format(archive_path, bad_file))
archive_file.close()

rm_tree(p/ext/'workingfiles')