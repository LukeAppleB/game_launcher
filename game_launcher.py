# need to read game json, display error if any
import json
import subprocess


def library(games):
    games['Games'] = sorted(games['Games'], key=lambda x: x['Title'])
    for game in games['Games']:
        print(game['Title'])


def get_game_location(input_title: str, games):
    for game in games['Games']:
        if str.lower(input_title) == str.lower(game['Title']):
            return game['Location']
        elif str.lower(input_title) in str.lower(game['Title']):
            print('Did you mean: ' + game['Title'] + '? (y/n)')
            did_you_mean_input = input()

            if did_you_mean_input == 'y' or did_you_mean_input == 'yes':
                return game['Location']
            else:
                continue

    print(f'No game found with name: {input_title}')
    return None


print('Welcome to Game Launcher')
print('Please enter the name of the game you would like to launch, or "list", "help", or "exit" to close')
cmd = None

while cmd != 'exit':
    cmd = input()

    with open('games.json') as file:
        games = json.load(file)

        if cmd == 'list':
            library(games)
        else:
            game_location = get_game_location(cmd, games)
            if game_location is not None:
                subprocess.run(game_location)
                exit()
