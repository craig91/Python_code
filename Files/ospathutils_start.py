import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
from xmlrpc.client import DateTime


def main():
    # print the name of the OS
    print(os.name)

    # # Check for item existence and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", path.isfile("textfile.txt"))
    print("Item is directory:", path.isdir("textfile.txt"))

    # # work with file paths
    print("Item's path", path.realpath("textfile.txt"))
    print("Item's path and name:", path.split(path.realpath("textfile.txt")))
    
    # Get the modification time
    t = time.ctime(path.getmtime('textfile.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('textfile.txt'))
    print("It has been", td, "Since the file was modified")
    print("Or,", td.total_seconds(), "seconds")
if __name__== "__main__":
    main()