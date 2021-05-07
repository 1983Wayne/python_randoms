### Classic anagrams checker, but using dictionary. ###

def check_if_anagram(string_1, string_2):
    legal_chars = 'abcdefghijklmnopqrstuvwxyz'
    string_1_dict = dict()
    string_2_dict = dict()
    
    for i in string_1.lower().replace(' ', ''):
        
        if i not in string_1_dict and i in legal_chars:
            string_1_dict[i] = 1
        else:
            string_1_dict[i] += 1
            
    for i in string_2.lower().replace(' ', ''):
        
        if i not in string_2_dict and i in legal_chars:
            string_2_dict[i] = 1
        else:
            string_2_dict[i] += 1
            
    if string_1_dict != string_2_dict:
            return 'These are not anagrams.'
        
    return 'These are anagrams.'
