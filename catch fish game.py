import random
import time
import string

def generate_hook(length=4):
    hook = ''.join(random.choices(string.ascii_letters, k=length))
    return hook

def easy_fish(hook):
    print(f"A fish is nibbling at your bait! Can you catch it?")
    print(f'Type this within 8 seconds: {hook}')
    start_time = time.time()
    user_input = input('Your answer: ')
    end_time = time.time()
    if end_time - start_time <= 8:
        if user_input.lower() == hook.lower():
            print('🎣 You caught the fish!')
        else:
            print('😢 The fish got away!')
    else:
        print('⏰ Time\'s up! The fish escaped!')

def normal_fish(hook):
    print(f"A fish is nibbling at your bait! Can you catch it?")
    print(f'Type this within 5 seconds: {hook}')
    start_time = time.time()
    user_input = input('Your answer: ')
    end_time = time.time()
    if end_time - start_time <= 5:
        if user_input.lower() == hook.lower():
            print('🎣 You caught the fish!')
        else:
            print('😢 The fish got away!')
    else:
        print('⏰ Time\'s up! The fish escaped!')

def hard_fish(hook):
    print(f"A fish is nibbling at your bait! Can you catch it?")
    print(f'Type this within 2 seconds: {hook}')
    start_time = time.time()
    user_input = input('Your answer: ')
    end_time = time.time()
    if end_time - start_time <= 2:
        if user_input.lower() == hook.lower():
            print('🎣 You caught the fish!')
        else:
            print('😢 The fish got away!')
    else:
        print('⏰ Time\'s up! The fish escaped!')

while True:
    mode = input('🌊 Welcome to the Fishing Game! Choose your level: Easy, Normal, or Hard? (Type your choice or anything else to quit): ').lower()
    if mode == 'easy':
        generated_hook = generate_hook()
        print(f'🔆 Easy mode is starting in 5 seconds... You have 8 seconds to type the word or the fish will escape: ')
        time.sleep(5)
        easy_fish(generated_hook)
    elif mode == 'normal':
        generated_hook = generate_hook()
        print(f'🌊 Normal mode is starting in 5 seconds... You have 5 seconds to type the word or the fish will escape: ')
        time.sleep(5)
        normal_fish(generated_hook)
    elif mode == 'hard':
        generated_hook = generate_hook()
        print(f'🔥 Hard mode is starting in 5 seconds... You have 2 seconds to type the word or the fish will escape: ')
        time.sleep(5)
        hard_fish(generated_hook)
    else:
        print('👋 Thanks for playing! Goodbye!')
        break