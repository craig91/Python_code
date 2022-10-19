def main():
    f = open("myile.txt", "w+")

    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()

    f = open("myile.txt", "r")
    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            print(x)

if __name__== "__main__":
    main()