def rot13(message: str):
    trans = ""
    for character in message:
        if character.isalpha():
            num = ord(character)
            num += 13
            if character.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num -= 26
            elif character.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            trans += chr(num)
        else:
            trans += character
    return trans
