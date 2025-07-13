import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




path = '/home/cdejeantsuno/Documents'
files_in_dir = os.listdir(path)
print("Files and directories in '", path, "' : ")
# print(files_in_dir)
print(type(files_in_dir))

for file in files_in_dir:
    print(file)

# cwd = os.getcwd()
# print(type(cwd))
# print(cwd)

# Documents = 'home/$USER/Documents'
# #Documents = '/home/cdejeantsuno/Code/Python_code'

# if cwd != Documents:
#     print("This is not the correct path")
#     cwd = os.chdir('../')
# else:
#     print("This is the correct Path")


# print(cwd)