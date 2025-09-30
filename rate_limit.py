count = 0 

def func():
    global count
    count += 1

func()
print("Number of function calls:", count)
