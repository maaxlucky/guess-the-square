
import random

files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # a-h
def generate_square():
    file = random.choice(files)
    rank = random.randint(1, 8)

    if files.index(file) % 2 == 0 and rank % 2 == 1 or files.index(file) % 2 == 1 and rank % 2 == 0:
        color = 'dark'
    else:
        color = 'light'

    return file, rank, color

def Main():
    file, rank, color = generate_square()
    ans = str(input(f'What color is {file}{rank}?\\n>> ')).lower()
    if ans == 'idk':
        print(f'{file}{rank} was a {color} square :(')
    elif ans != 'dark' and ans != 'light':
        print('Not right')
    elif ans == color:
        print('Correct!!')
        return Main()
    else:
        print(f'Incorrect, {file}{rank} was a {color} square :(')

Main()
