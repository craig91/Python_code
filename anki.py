def func():
    def nested():
        def nested2():
            nonlocal x # -> binds to closest enclosing variable: nested() -> 50
            x = 100 #--> changes from 50 to 100
            print("nested2:", x) # -> 100 
        x = 50 #--> local to nested()
        nested2() # -> should print 100
        print("nested:", x) # -> should print 50
    x = 10 # local to func()
    nested()
    print("func:", x) # unchanged by nested(), nested2()

x = 1 # global x
func()
print("outer:", x) # -> will print 1
