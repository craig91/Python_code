import tkinter

window_main = tkinter.Tk(className = 'Tkinter - Example', )
window_main.geometry("400x200")

def submitFunction():
    print('Submit button in clicked')

button_submit = tkinter.Button(window_main, text='Submit', command=submitFunction)
button_submit.config(width=20, height=2)

button_submit.pack()
window_main.mainloop()