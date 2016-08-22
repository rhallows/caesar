#Defines a function that will recieve a letter and return the 0 based positon of the letter within the alphabet

def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = ''

    for char in letter:
        position = alphabet.index(char) + 1
        return position


### 1. figure out chars position  2. add rot to answer 3. use chr to get new char 4. return
def rotate_character(char, rot):
    get_alpha_position = ''

    ### Gets the chars index value for where the char is in the alphabet.
    for i in char:
        get_alpha_position = alphabet_position(char.lower())

    ### Adds the rotation number to the index value of where the char is in the alphabet
    add_rot = get_alpha_position + rot

    ### Checks to see if the add_rot value is out of the range of letters in teh alphabet. If it is, use modulo to bring it back in range
    if add_rot > 26:
        new_position = add_rot % 26
        if char.isupper():
            return chr(64 + new_position)
        else:
            return chr(96 + new_position)
    elif char.isupper():
            return chr(64 + add_rot)
    else:
            return chr(96 + add_rot)


###This is the main. 1.It should figure out the case of character 2. It should rotate character
def encrypt(text, rot):
    encrypted_string = ''
    for char in text:
        if char.isalpha():
            new_char = rotate_character(char, rot)
            encrypted_string += new_char
        else:
            encrypted_string += char
    return encrypted_string


###Gets console input from user to declare variables and call function
#textString = input("Type a message that you would like to encrypt: ")
#rot = int(input("Type an integer value to rotate the letter position by: "))
#print(encrypt(textString, rot))
