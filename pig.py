import random

def roll():
    min_role = 1
    max_role = 6
    roll = random.randint(min_role, max_role)


    return roll

while True:
    players = input("How many players? (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= (players) <= 4:
            print(f'{players} players are playing')
            break
        else:
            print('Choose between (2-4)')
    else:
        print('invalid input')


player = [0 for _ in range(players)]
max_score = 50


while max(player) <= max_score:
    for player_idx in range(players):
        print(f'Its Player {player_idx+1} turn')
        print("\nYour score is: ", player[player_idx], '\n')

        current_score = 0

        while True:
            should_role = input("do u wanna continue rolling? (y): ")
            if should_role.lower() != 'y':
                break

            value = roll()

            if value == 1:
                print('You rolled 1, start from 0')
                current_score = 0
                break

            else:
                current_score += value
                print(f'You rolled a {value}')

            print(f'\nYour score is now {current_score}\n')


        player[player_idx] += current_score
        print (f"your total score is {player[player_idx]}")


max_score = max(player)
winning_idx = player.index(max_score)
print(f"player {winning_idx+1} won the game with the score of {max_score}")