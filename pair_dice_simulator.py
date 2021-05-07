import random

def simulate(amount):
    "Simulates 'amount' of dice rolls and returns percentages of rolled total."
    
    two_dice = {}

    for i in range(2, 13):
        two_dice[str(i)] = 0
    
    for i in range(1, amount + 1):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        two_dice[str(die_1 + die_2)] += 1
   
    print("{:<8} {:<15}".format('Total','Simulated'))
    
    for total, throws in two_dice.items():
        sim = throws / (amount / 100)
        print ("{:<8} {:<15}".format(total, sim))
