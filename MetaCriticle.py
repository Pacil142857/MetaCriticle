import random
from MetaCritic.MetaCriticScraper import MetaCriticScraper

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
        'https://www.metacritic.com/game/wii/super-smash-bros-brawl',
        'https://www.metacritic.com/game/wii/the-legend-of-zelda-skyward-sword',
        'https://www.metacritic.com/game/wii/xenoblade-chronicles',
        'https://www.metacritic.com/game/wii/rayman-origins',
        'https://www.metacritic.com/game/wii/new-super-mario-bros-wii',
        'https://www.metacritic.com/game/wii/kirbys-epic-yarn',
        'https://www.metacritic.com/game/wii/lego-star-wars-the-complete-saga',
        'https://www.metacritic.com/game/wii/wii-sports-resort',
        'https://www.metacritic.com/game/wii/mario-party-9',
        'https://www.metacritic.com/game/wii/animal-crossing-city-folk']

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
            if (game['critic_score'] == solutionGames[-1]['critic_score']):
                solutionGames.pop()
                scoreUnique = False
                break

        # Remove the entry from urls
        if (scoreUnique):
            urls.remove(curGame)
            
    # Get the distractor games
    distractorGames = random.sample(urls, 20)
    
    return [solutionGames, distractorGames]


