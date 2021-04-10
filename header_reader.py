def header_reader():
    """Will read only the first 10 lines."""
    print("This program reads the first ten lines of a text file for you.")

    filename = input("What filename did you want to open? >    ")
    f_in = open(filename, "r")

    header_range = 10
    line_on = 0

    while line_on < header_range:
        line = f_in.readline()
        print(f"This is line {line_on}")
        print(line)
        line_on += 1
   
def write_file():
    """This function will make you a quick grid of 100 x 100 items to read."""
    file_new = "input.txt"
    f_in = open(file_new, "w")

    for i in range(100):
        for j in range(100):
            tup = (i, j)
            f_in.write(str(tup))
        f_in.write("\n")
