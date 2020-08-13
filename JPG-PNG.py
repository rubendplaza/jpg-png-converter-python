import os
from PIL import Image

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
