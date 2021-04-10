# This program will look through a text file and collect and print out the length and words that are most abundant.

fin = input("What file did you want to read in? >  ")
file_in = open (fin, "r")
longest_word = "a"
longest_words_list = ["a"]

for line in file_in:
    for strang in line.split():
        current_string = strang.lower()
        if len(current_string) > len(longest_word):
            longest_words_list = []
            longest_word = current_string
            longest_words_list.append(current_string)
            
        elif len(current_string) == len(longest_word):
            if current_string not in longest_words_list:
                longest_words_list.append(current_string)
            
for item in longest_words_list:
    if len(item) != len(longest_word):
        longest_words_list.remove(item)
        
print(f"The largest words of length {len(longest_word)} are: ")
for item in longest_words_list:
    print(item)
            
        
