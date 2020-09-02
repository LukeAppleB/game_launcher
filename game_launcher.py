import json
import os
import subprocess


# TODO:
# fix bug where games added in the software are sorted improperly in the list

game_json_location = "C:/dev/game_launcher/games.json"

def library(games, show_all: bool = False):
    games['Games'] = sorted(games['Games'], key=lambda x: x['Title'])
    for game in games['Games']:
        title = game['Title']
        location = game['Location']

        if show_all:
            print(f'Title: {title} - Location: {location}')
        else:
            print(game['Title'])


def add_game(games):
    print('Enter the title of the game you would like to add:')
    title = input()

    print('Enter / paste the location of the exe, or lnk file:')
    location = input()

    if '.exe' not in location and '.lnk' not in location:
        print('WARNING - Your location does not point to one of the required filetypes !')

    print(f'You are adding the game {title}, located at {location}. Are you sure? (y/n)')
    are_you_sure = input()

    if are_you_sure == 'y' or are_you_sure == 'yes':
        games["Games"].append({'Title': f'{title}', 'Location': f'{location}'})
        with open(game_json_location, 'w') as outfile:
            json.dump(games, outfile)


def display_help():
    print('---------------- HELP MENU ----------------')
    print('Available commands:')
    print('"list" - Displays all the titles in your library')
    print('"list -a" - Displays all the titles in your library, and their install locations')
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

        elif str.lower(cmd) == 'list -a':
            library(games, True)

        elif str.lower(cmd) == 'add':
            add_game(games)

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
