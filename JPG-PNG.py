# python3 JPG-PNG.py Pokedex/ new/
# takes in two arguments, the folder where the jpg pics are and a folder where the png pics will be placed

import sys
import os
from PIL import Image

# using sys, grab first and second args
# check if new/ exists, if not, create it
# loop through the jpg folder and then convert each image to png
# save them to the new folder

# how to use sys module to grab command line arguments
# how to us os or pathlib module to grab path so that you can create files and suc
# converting to png with pillow

curr_dir = './' + \
    input('Enter the name of the folder your JPG images are in: ')
new_dir = './' + \
    input('Enter the name of the folder you want your PNG images to be in: ')

if not os.path.isdir(curr_dir):
    print('The JPG directory does not exist. Create it.')
    exit()

if not os.path.isdir(new_dir):
    print(f'Creating directory {new_dir}')
    os.mkdir(new_dir)

print('')

for entry in os.scandir(curr_dir):
    if entry.path.endswith(".jpg") and entry.is_file():
        file_name = os.path.split(entry.path)[-1]
        print('Converting: ' + os.path.split(entry.path)[-1])
        img = Image.open(entry.path)
        base = os.path.splitext(file_name)[0]
        new_file_path = new_dir + '/' + base + '.png'
        print('Creating: ' + new_file_path + '\n')
        img.save(new_file_path, 'png')
