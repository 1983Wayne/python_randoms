# This code randomly generates 'coin flips' until heads or tails comes up three
# times in a row.  When that happens, it records the amount of flips in a total
# and proceeds to do it amount - 1 more times. After 100,000 times, it converges
# on 7.

import random
def three_flips(amount):
    "Function that simulates coin-tosses for 'amount' of times."
    total_flips = 0
    for i in range(amount):
        tails = False
        heads = False
        times = 0
        flips = 0
        while times < 3:
            coin_toss = random.randint(0, 1)
            flips += 1
            if coin_toss == 0 and tails == True:
                times += 1
            elif coin_toss == 0 and tails == False:
                times = 1
                tails = True
                heads = False
            elif coin_toss == 1 and heads == True:
                times += 1
            else:
                times = 1
                heads = True
                tails = False
            if coin_toss == 0:
                print('H', end=' ')
            else:
                print('T', end=' ')
        print('(', flips, 'flips )')
        total_flips += flips
    print('On average,', (total_flips / amount), 'flips were needed.')
