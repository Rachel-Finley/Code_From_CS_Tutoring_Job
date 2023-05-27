# Assignment 8

def cipher(x):
    Newx = ""
    cipherKeys = []

    for index in range(len(x)):
        cipherKeys.append(ord(x[index]))
        Newx += chr(ord(x[index]) + cipherKeys[index])

    return Newx, cipherKeys

def decipher(x, keys):
    actualLetter = ""

    for index in range(len(x)):

        actualLetter += chr(ord(x[index]) - keys[index])

    return actualLetter


def main():
    user_string = ""

    user_string = input("Enter a string for encryption:")
    print("Your input is:", user_string)

    encrypted, cipherKeys = cipher(user_string)
    print('Your encrypted string is:', encrypted)

    decrypted = decipher(encrypted, cipherKeys)
    print('Your decrypted string is:', decrypted)


main()