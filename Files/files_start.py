def main():
    # Open a file for writing and create it if it doesn't exist
    myfile = open("textfile.txt", "w+")

    # Open the file for appending text to the end

    # write some lines of data into the file
    for i in range(10):
        myfile.write("This is some text\n")
    # close the file when done
    myfile.close()



    if __name__ == "__main__":
        main()