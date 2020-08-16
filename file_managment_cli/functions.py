import os
import glob
import shutil

""" 
This func removes all .png files from my desktop, as I often spend time sending screen shots around to colleagues and deleting 1 by 1 is annoying
"""


def clear_desktop_of_pngs():
    path = glob.glob("/Users/pb/desktop/*.png")

    for f in path:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def move_files():
    src = "/Users/paul/Desktop/py_move/old"
    dest = "/Users/paul/Desktop/py_move/new"

    files = os.listdir(src)

    for file in files:
        new_path = shutil.move(f"{src}/{file}", dest)
        print(new_path)
