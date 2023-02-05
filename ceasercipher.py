def ccipher():
    final=[]
    wordcc=input("Please input a word for ciphering.Uppercase only:")
    shift=int(input("Please input a shift for ciphering:"))
    for i in range(0,len(wordcc)):
        if wordcc[i].isupper:
            letter=chr((ord(wordcc[i]) + shift+65) % 26 + 65)
        else:
            letter=chr((ord(wordcc[i]) + shift+97) % 26 + 97)
        final.append(letter)
    print(''.join(final))
ccipher()
