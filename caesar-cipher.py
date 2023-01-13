alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
 , 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #alphabet twice to avoid error with last letters

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): # the text and the shift amount 
    cipher_text = ""
   
    for letter in plain_text: # for each letter in the text :
        position = alphabet.index(letter) #know the position of the word in the alphabet list 
        newposition = position + shift_amount # set the new position to position + shift
        newletter = alphabet[newposition]
        cipher_text += newletter
    print(cipher_text)


def decrypt(plain_text, shift_amount): #here will do the opposite
    cipher_text = ""

    for letter in plain_text: # for each letter in the text :
        position = alphabet.index(letter) #know the position of the word in the alphabet list 
        newposition = position - shift_amount # set the new position to position + shift
        newletter = alphabet[newposition]
        cipher_text += newletter
    print(cipher_text) 

if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction =="decode":
    decrypt(plain_text=text,shift_amount=shift)