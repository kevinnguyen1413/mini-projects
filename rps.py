import random
def main():
    player = input('Rock, Paper, or Scissors?\nPlayer: ').lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    rps(player, computer)
    
def rps(player, computer):
    assign = {'rock':0, 'paper':1, 'scissors':2}
    outcome = ['Draw!', 'Player won!', 'Computer won!']
    print(f'Computer: {computer.title()}')
    return print(outcome[assign[player]-assign[computer]])

main()