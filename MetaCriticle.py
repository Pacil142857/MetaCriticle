import random
from flask import Flask, flash, redirect, render_template, request, session
from functools import wraps
from MetaCritic.MetaCriticScraper import MetaCriticScraper
from tempfile import mkdtemp

urls = ['https://www.metacritic.com/game/nintendo-64/tony-hawks-pro-skater-2',
        'https://www.metacritic.com/game/nintendo-64/mario-party-3',
        'https://www.metacritic.com/game/nintendo-64/paper-mario',
        'https://www.metacritic.com/game/nintendo-64/mega-man-64',
        'https://www.metacritic.com/game/nintendo-64/banjo-tooie',
        'https://www.metacritic.com/game/nintendo-64/kirby-64-the-crystal-shards',
        'https://www.metacritic.com/game/nintendo-64/donkey-kong-64',
        'https://www.metacritic.com/game/nintendo-64/mario-golf',
        'https://www.metacritic.com/game/nintendo-64/pokemon-snap',
        'https://www.metacritic.com/game/nintendo-64/super-smash-bros',
        'https://www.metacritic.com/game/wii/super-mario-galaxy',
        'https://www.metacritic.com/game/wii/the-legend-of-zelda-skyward-sword',
        'https://www.metacritic.com/game/wii/xenoblade-chronicles',
        'https://www.metacritic.com/game/wii/rayman-origins',
        'https://www.metacritic.com/game/wii/new-super-mario-bros-wii',
        'https://www.metacritic.com/game/wii/kirbys-epic-yarn',
        'https://www.metacritic.com/game/wii/lego-star-wars-the-complete-saga',
        'https://www.metacritic.com/game/wii/wii-sports-resort',
        'https://www.metacritic.com/game/wii/mario-party-9',
        'https://www.metacritic.com/game/wii/animal-crossing-city-folk',
        'https://www.metacritic.com/game/pc/speedrunners',
        'https://www.metacritic.com/game/pc/valkyria-chronicles',
        'https://www.metacritic.com/game/pc/among-us',
        'https://www.metacritic.com/game/playstation-4/fall-guys-ultimate-knockout',
        'https://www.metacritic.com/game/pc/team-fortress-2',
        'https://www.metacritic.com/game/ios/bloons-td-5',
        'https://www.metacritic.com/game/playstation-4/xcom-2',
        'https://www.metacritic.com/game/switch/return-of-the-obra-dinn']

# Get the solution games and distractor games
# Format: [solutionGames, distractorGames]
def getGames():
    solutionGames = []
    curGame = ''
    scoreUnique = True
    
    # Get the solution games
    while len(solutionGames) < 6:
        curGame = random.choice(urls)
        solutionGames.append(MetaCriticScraper(curGame))
        scoreUnique = True
        
        # Ensure this game has a unique score
        for game in solutionGames[:-1]:
            if (game.game['critic_score'] == solutionGames[-1].game['critic_score']):
                solutionGames.pop()
                scoreUnique = False
                break

        # Remove the entry from urls
        if (scoreUnique):
            urls.remove(curGame)
            
    # Get the distractor games
    distractorGames = [MetaCriticScraper(game) for game in random.sample(urls, 20)]
    
    return [solutionGames, distractorGames]


# Check if a response is correct or not
# Returns an array of numbers: 0s are gray, 1s are yellow, and 2s are green
def checkResponse(responseTitles, solution):
    feedback = []
    solutionTitles = [game.game['title'] for game in solution]
    # responseTitles = [game.game['title'] for game in response]
    
    for i in range(len(responseTitles)):
        # Check if this part of the response is correct
        if responseTitles[i] == solutionTitles[i]:
            feedback.append(2)
            continue
        # Check if the game appears somewhere in the solution
        elif responseTitles[i] in solutionTitles:
            feedback.append(1)
        # The game is not in the solution
        else:
            feedback.append(0)
    
    return feedback

def intInput(prompt, min, max):
    inputGood = False
    uInput = None
    while not inputGood:
        uInput = input(prompt)
        try:
            uInput = int(uInput)
            assert uInput >= min
            assert uInput <= max
            inputGood = True
        except:
            continue
    
    return uInput

gameEnded = False
confirmSelection = False
userSelection = []
solution, distractors = getGames()
games = [item.game['title'] for item in solution] + [item.game['title'] for item in distractors]
games.sort()
hints = [' '] * 26

# Main loop
print(games)
while not gameEnded:
    # Print the available games
    for i in range(len(games)):
        print(f'[{hints[i]}] {i + 1}: {games[i]}')
    
    # Print the scores of the solution
    print([item.game['critic_score'] for item in solution])
    
    # Get the user's input
    for i in range(6):
        userSelection.append(games[intInput(f'Game {i + 1}: ', 1, len(games)) - 1])
    
    check = checkResponse(userSelection, solution)
    
    # Update games
    for i, hint in enumerate(check):
        if hint == 0:
            del hints[games.index(userSelection[i])]
            games.remove(userSelection[i])
        elif hint == 1:
            hints[games.index(userSelection[i])] = '?'
        elif hint == 2:
            hints[games.index(userSelection[i])] = str(i + 1)
    
    userSelection = []

'''
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Ensure that responses aren't cached
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = 0
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route('/')
def index():
    solution, distractors = getGames()
    solImages = [item.game['image'] for item in solution]
    disImages = [item.game['image'] for item in distractors]
    images = (solImages + disImages).sort()
    return render_template('index.html', images=images)
'''
