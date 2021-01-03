### A Python Program to convert an input string into the amount of keystrokes needed to display your word. ###
### For example : "Hello World!" takes the key presses : 44335555556660966677755531111                     ###
##############################################################################################################

symbols = {'.,?!:' : 1, 'abc' : 2, 'def' : 3, 'ghi' : 4, 'jkl' : 5, 'mno' : 6,
           'pqrs': 7, 'tuv' : 8, 'wxyz': 9, ' ' : 0,}

def get_index_and_amount(letter, dictionary):
    "Helper function."
    
    for item in dictionary:
        if letter in item:
            key = item
            index = item.index(letter) + 1
            
    return str(dictionary[key]) * index

def get_full_string(string, dictionary):
    "Use this function to convert the string into digits presses."
    return_string = ''
    
    for i in string.lower():
        return_string += get_index_and_amount(i, dictionary)
        
    return return_string
