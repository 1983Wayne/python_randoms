### A small program to convert to and from simple morse code. ###

morse_table = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
              'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'}

def encode_string(string, table):
    dashes_dots = ''
    for i in string.lower():
        if i in table:
            dashes_dots += table[i]
            dashes_dots += ' '
    return dashes_dots

def decode_string(string, table):
    return_string = ''
    morse_list = string.split()
    for i in morse_list:
        for key in table:
            if table[key] == i:
                return_string += key
    return return_string
