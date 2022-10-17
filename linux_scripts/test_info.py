import tkinter as tk
import subprocess

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])

    
def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()