from optparse import OptParseError
import random

def play():
    user = input("Pick you choice ->'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "lost"

# r > s, s > p, p > r
# returns true if player wins
def is_win(player, cpu):
    if (player == 'r' and cpu == 's') or (player == 's' and cpu =='p') or (player == 'p' and cpu == 'r'):
       return  True

print(play()) 