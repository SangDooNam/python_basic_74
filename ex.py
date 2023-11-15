import random
from execptions import CoinError


check_guess = CoinError()
guess = ''

while guess not in ('heads', 'tails'):
    # print('Guess the coin toss! Enter heads or tails:')
    guess = check_guess.check('Guess the coin toss! Enter heads or tails: ')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = check_guess.check('Enter "heads" or "tails": ')
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')



