def do_twice(f, t ='test'):
    f(t)
    f(t)



def print_spam():
    print('spam')


do_twice(print_spam, 'v')
