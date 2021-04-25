def check_letters(grade):
    number_value = 0.0
    
    if grade[0].lower() == "a":
        number_value += 4.0
    elif grade[0].lower() == "b":
        number_value += 3.0
    elif grade[0].lower() == "c":
        number_value += 2.0
    elif grade[0].lower() == "d":
        number_value += 1.0
    elif grade[0].lower() == "f":
        return "FAILURE"
    else:
        return "Over 9000"
    
    if len(grade) > 1:
        
        if grade[1] == "+":
            if number_value != 4.0:
                number_value += 0.3
                
        elif grade[1] == "-":
            number_value -= 0.3
        
    return number_value

def convert_to_letter(grade):
    letter_grade = ""
    if 1.0 <= grade <= 1.3:
        letter_grade += "D"
    elif 1.7 <= grade <= 2.3:
        letter_grade += "C"
    elif 2.7 <= grade <= 3.3:
        letter_grade += "B"
    elif 3.7 <= grade <= 4.0:
        letter_grade += "A"
    if round((grade - int(grade)), 1) == 0.3:
        letter_grade += "+"
    elif round((grade - int(grade)), 1) == 0.7:
        letter_grade += "-"
    if letter_grade == "":
        letter_grade = "You screwed the number up on this one."
    return letter_grade
        
def check_grades():
    """Program will convert either a letter grade to a Floating point scale
    or from a float style to a letter grade.  The program will accept one
    grade per line and then when finished, will read the contents of the list 
    created back to the user."""
    empty_line = False
    grades_list = []
    print("This program will take any input, but mistakes will be lightly tolerated!")
    while not empty_line:
        value = input("You can input any number of grades in either decimal or letter format.  Empty line to quit.")
        
        if value == "":
            break
        
        elif len(value) == 3:
            try:
                grades_list.append(convert_to_letter(float(value)))
            except:
                grades_list.append("Error on conversion")
                
        elif type(value) == str:
            grades_list.append(check_letters(value))
    return grades_list
        
