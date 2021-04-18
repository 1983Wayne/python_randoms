def main():
  """Adds numbers as the user enters them, and catches an exception if the entered number
  is not a float.  Quit is accomplished by entering a space."""
  
    print("This program will add your input numbers and print them out.")
    space_break = False
    number_total = 0
    while not space_break:
        print("Your number total is at", number_total)
        number_added = input("Enter a space to quit, or enter a number to add >  ")
        
        if number_added != " ":
            try: 
                number_added = float(number_added)
                number_total += number_added
            
            except:
                print("You need to enter a valid number or a space.")
        
        else:
            print("Quitting now.")
            space_break = True
        
if __name__ == "__main__":
    main()
