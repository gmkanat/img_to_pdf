import os.path
from PIL import Image
from os import listdir
from os.path import isfile, join
import random
import string
abs_path = '/home/admin/Documents/'

d = {}


def get_random_name():
    return ''.join(random.choice(string.ascii_letters) for i in range(10)) + '.pdf'


def get_all_jpg(files, path):
    jpg_files = []

    for file in files:
        if isfile(join(path, file)):
            if file.endswith(".JPG"):
                jpg_files.append(file)
    return jpg_files


def img_to_pdf(files, path):
    # get all jpg files in the directory
    jpg_files = get_all_jpg(files, path)
    # if it contains jpg
    if len(jpg_files) > 0:
        # we sort it by name
        jpg_files.sort()
        jpged = []
        # make it as Image objects
        # to convert it first gets the image object, then like extends
        im_1 = Image.open(join(path, jpg_files[0]))
        im_1 = im_1.convert('RGB')
        for file in range(1, len(jpg_files)):
            f = Image.open(join(path, jpg_files[file]))
            f = f.convert('RGB')
            jpged.append(f)
        # save file with random name in current directory
        im_1.save(join(path, get_random_name()), 'pdf', save_all=True, append_images=jpged)


def dfs(path):
    # simple dfs algorithm to traverse the directory
    d[path] = 1
    for f in listdir(path):
        # check if the path is a directory
        if os.path.isdir(join(path, f)):
            # if it is, call dfs on it
            dfs(join(path, f))
            # if it is a file, convert all jpg files to pdf in current directory
            if len(listdir(join(path, f))):
                img_to_pdf(listdir(join(path, f)), join(path, f))


if __name__ == '__main__':
    dfs(abs_path)
