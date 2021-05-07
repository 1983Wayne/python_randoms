import random

def create_bingo_card():
    "This function creates a random BINGO card for a player."
    card = {"B": [], "I": [], "N": [], "G": [], "O": []}
    max_range = 15
    low_range = 1

    for key in card:
        while len(card[key]) < 5:
            integer = random.randint(low_range, max_range)
            
            if len(card[key]) == 2 and key == "N":
                card[key].append("FREE")
                
            elif integer not in card[key]:
                card[key].append(integer)
                
        low_range = max_range + 1
        max_range += 15
    return card


def check_horizontals(card): # Check only for horizontal win conditions
    "Starts at the top row and checks from there."
    for i in range(5):
        total = 0
        for key in card:
            if type(card[key][i]) == int:
                total += card[key][i]
            else:
                total += 0
        if total == 0:
            return True
    return False

def check_verticals(card): # Check only for vertical win conditions
     "Starts at the left and moves right."
     card['N'][2] = 0
     for key in card:
          if sum(card[key]) == 0:
            return True
     return False
        
def check_card(card):
    if check_horizontals(card):
        return ("You've won on the horizontals!")
    elif check_verticals(card):
        return ("You've won on the verticals!")
    else:
        return ("This was not a winning card, better luck next time!")
