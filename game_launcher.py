# need to read game json, display error if any
import json


def library(games):
    for game in games['Games']:
        print(game['Title'])

def cmd_is_game_title(input_title: str):
    pass

print('Welcome to Game Launcher')
print('Please enter the name of the game you would like to launch, or "list", "help", or "exit" to close')
cmd = None


while cmd != 'exit':
    cmd = input()

    with open('games.json') as file:
        games = json.load(file)

        if cmd == 'list':
            library(games)

        if cmd_is_game_title(cmd):
            pass




# prompt for either list or name of game, or add/remove

# have tab autofill similar to unix


