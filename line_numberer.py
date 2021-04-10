def reprint_lines(file):
    """Takes an output file and numbers the input file lines into it."""
    output = open("output.txt", "w")
    number_on = 1
    file_lines = file.readlines()
    changed_lines = ""
    
    for line in file_lines:
        changed_lines += f"{number_on} " + line
        number_on += 1
        
    output.write(changed_lines)
        

        
file_in = input("What file did you want to read and number? >  ")

fin = open(file_in, "r")

reprint_lines(fin)
