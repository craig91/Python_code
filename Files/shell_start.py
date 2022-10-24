import os
from os import path
import shutil

def main():
    # make duplicate of existing file
    if path.exists('textfile.txt'):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")
        # let's make a backup copy by appending "sh" to the name
        dst = src + ".sh"
        shutil.copy()
        

        # rename the original file


        # now put things into a ZIP archive


        # more fine-grained control over ZIP files



if __name__== "__main__":
    main()