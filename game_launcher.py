import json
import os
import subprocess

game_json_location = "C:/dev/game_launcher/games.json"

def library(games):
    games['Games'] = sorted(games['Games'], key=lambda x: x['Title'])
    for game in games['Games']:
        print(game['Title'])


def display_help():
    print('---------------- HELP MENU ----------------')
    print('Available commands:')
    print('"list" - Displays all the titles in your library')
    print('"help" - Displays the menu you are looking at now')
    print('"exit" - Closes the program')
    print('It will be assumed that anything else entered, is the title of a game you are trying to launch')
    print('')


def get_game_location_with_name(input_title: str, games):
    for game in games['Games']:
        if str.lower(input_title) == str.lower(game['Title']):
            return game['Location']
        elif str.lower(input_title) in str.lower(game['Title']):
            print('Did you mean: ' + game['Title'] + '? (y/n)')
            did_you_mean_input = input()

            if did_you_mean_input == 'y' or did_you_mean_input == 'yes':
                return game['Location']

    print(f'No game found with name: {input_title}')
    return None


print('Welcome to Game Launcher')
print('Please enter the name of the game you would like to launch, or "list", "help", or "exit" to close')
cmd = None

while cmd != 'exit':
    cmd = input()
    if cmd == '':
        continue

    with open(game_json_location) as file:
        games = json.load(file)

        if str.lower(cmd) == 'list':
            library(games)
        elif str.lower(cmd) == 'help':
            display_help()
        else:
            game_location = get_game_location_with_name(cmd, games)
            if game_location is not None:
                if '.lnk' in game_location:
                    os.startfile(game_location)
                else:
                    subprocess.run(game_location)
                exit()
