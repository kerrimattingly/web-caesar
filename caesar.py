def alphabet_position(letter):

    lower_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if letter in lower_alpha:
        return lower_alpha.index(letter)
    elif letter in upper_alpha:
        return upper_alpha.index(letter)
    else:
        return None

def rotate_character(char,rot):

    lower_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    new_char = ""
    first_num = alphabet_position(char)
    if char in lower_alpha:
        new_index = (first_num + rot) % 26
        new_char = lower_alpha[new_index]
    elif char in upper_alpha:
        new_index = (first_num + rot) % 26
        new_char = upper_alpha[new_index]
    else:
        return char
    return new_char

def encrypt(text,rot):

    new_str = ""
    for a_char in text:
        encrypted_char = rotate_character(a_char,rot)
        new_str = new_str + encrypted_char
    return new_str
