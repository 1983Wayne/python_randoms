# This program will count the letters up in a text file and print them out for you.

fin = input("What file did you want to read in? >  ")
file_in = open (fin, "r")
letters_acceptable = 'abcdefghijklmnopqrstuvwxyz'
letter_list = {}

for line in file_in:
    for strang in line.split():
        for letter in strang:
            current_letter = letter.lower()
            if current_letter in letter_list and current_letter in letters_acceptable:
                
                letter_list[current_letter] += 1
            elif current_letter in letters_acceptable:
                letter_list[current_letter] = 1

print(letter_list)
