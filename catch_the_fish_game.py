import random
import time
import string
import asyncio
import aioconsole

def generate_hook(length=4):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

async def catch_fish(timeout, hook):
    print(f"A fish is nibbling at your bait! Can you catch it?")
    print(f'Type this within {timeout} seconds: {hook}')
    
    try:
        user_input = await asyncio.wait_for(aioconsole.ainput("Your answer: "), timeout)
        if user_input == hook:
            print('🎣 You caught the fish!\n')
        else:
            print('😢 The fish got away!\n')
    except asyncio.TimeoutError:
        print('\n⏰ Time\'s up! The fish escaped!\n')

async def main():
    while True:
        mode = await aioconsole.ainput('🌊 Welcome to the Fishing Game! Choose your level: Easy, Normal, or Hard? (Type your choice or anything else to quit): ')
        mode = mode.lower()
        if mode == 'easy':
            generated_hook = generate_hook()
            print(f'🔆 Easy mode is starting in 3 seconds... You have 8 seconds to type the word or the fish will escape: ')
            time.sleep(3)
            await catch_fish(8, generated_hook)
        elif mode == 'normal':
            generated_hook = generate_hook()
            print(f'🌊 Normal mode is starting in 3 seconds... You have 5 seconds to type the word or the fish will escape: ')
            time.sleep(3)
            await catch_fish(5, generated_hook)
        elif mode == 'hard':
            generated_hook = generate_hook()
            print(f'🔥 Hard mode is starting in 3 seconds... You have 2 seconds to type the word or the fish will escape: ')
            time.sleep(3)
            await catch_fish(2, generated_hook)
        else:
            print('👋 Thanks for playing! Goodbye!!')
            break

if __name__ == '__main__':
    asyncio.run(main())
