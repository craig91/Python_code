def pig_latin():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input('enter your word here ').lower()
    first_letter_sliced = slice(1)
    first_letter = word[first_letter_sliced]
    
    for vowel in vowels:
        #print(vowel)
        #print(first_letter)
        #print(word)
        if first_letter == vowel:
            print("matched!")
            exit()
        else:
            print("doesn't match!")


pig_latin()

