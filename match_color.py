import random

COLORS = ['W', 'B', 'R', 'G', 'Y', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    return code
def guess_code():
    while True:
        guess = input("\nGuess (space separated): ").upper().split()
        if len(guess) != CODE_LENGTH:
            print(f"Invalid, you must guess {CODE_LENGTH} colors")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid {color}, you must guess from the list. Try again")
                break
        else:
            break
        
    return guess

def check_colors(guess, real_colors):
    color_counts = {}
    correct_colors = 0
    incorrect_colors = 0
    for color in real_colors:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
    for guess_color, real_color in zip(guess, real_colors):
        if guess_color == real_color:
            correct_colors += 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_colors):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_colors += 1
            color_counts[guess_color] -= 1
            
    return correct_colors, incorrect_colors

def game():
    print(f"Welcome to color guessing game. You have {TRIES} attempts to guess")
    print('The valid colors are', '(', *COLORS,')')
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        guess = [color.upper() for color in guess]
        correct_colors, incorrect_colors = check_colors(guess, code)
        
        if correct_colors == CODE_LENGTH:
            print(f'You guessed colors in {attempts} attempts')
            break
        
        print(f'Correct position: {correct_colors}, Incorrect position: {incorrect_colors} ... {attempts}/{TRIES} Tries')
        
    else:
        print('You ran out of tries. The correct code was ',  {*code})
if __name__ == "__main__":
    game()