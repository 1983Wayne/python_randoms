#Takes any text document and will find the most popular word in it.

def main(file_in):
    
    file_in = open("sample.txt", "r")
    word_dict = {}
    for line in file_in:
        words = line.split()
        for word in words:
            word = word.lower().strip(" ,.!';/")
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
            
    for word in sorted(word_dict):
        print(word, word_dict[word])
    
    
    MaxKey = max(word_dict, key=word_dict.get)
    print("The most frequent word is:", MaxKey, "and the amount of it is: ", word_dict[MaxKey])
    
    file_in.close()

file_wanted = input("What is the path of the text file? *.txt only: ")

main(file_wanted)
