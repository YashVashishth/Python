alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaserCypher(Start_text,shift,direction):
    endText = ""
    for letter in Start_text:
        pos = alphabet.index(letter)
        if(direction=="encode"):
            wantedPos = pos+shift
        else:
            wantedPos = pos-shift
        wantedLetter = alphabet[wantedPos]  
        endText = endText+wantedLetter
    print(f"The Requested text is {endText} ")  

shouldContinue = True    
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    char = "a"
    asii_value = ord(char)
    #print(char)
    #print(asii_value)
    #print(asii_value + 3)
    shift = shift % 26     

    ceaserCypher(text,shift,direction)
    wannaContinue = input(f"Do you wanna go again type 'Yes' or 'No' ")
    if(wannaContinue == "Yes"):
        shouldContinue = True
    else:
        shouldContinue = False
        print("GoodBye")



'''def encrypt(plainText,shift_Amount,alphabet):
    cypherText = ""
    for letter in plainText:
        
        position = alphabet.index(letter)
        newPosition = position+shift
        newLetter = alphabet[newPosition]
        cypherText = cypherText+newLetter
    print(f"The encoded message is {cypherText}")    



def decrypt(secretText,shift_Amount,alphabet):
    decypherText = ""
    for letter in secretText:
        cypher_pos = alphabet.index(letter)
        earlierPos = cypher_pos-shift
        earlierLetter = alphabet[earlierPos]
        decypherText = decypherText+earlierLetter
    print(f"The decypered text is {decypherText}")


if(direction=="encode"):
    encrypt(text,shift,alphabet)
else:
    decrypt(text,shift,alphabet)'''



    






    




