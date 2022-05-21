# Metacritic Python API
You can parse user-score, critic-score, and other information from html of metacritic.com using this codes. 
   
## Usage
## How To Use

### Import 
```python
from MetaCriticScraper import MetaCriticScraper
```
### Example 
* Code
```python
urlForHorizonZeroDawn = 'https://www.metacritic.com/game/pc/horizon-zero-dawn-complete-edition?ref=hp'
scraper = MetaCriticScraper(urlForHorizonZeroDawn)
print("URL: " + scraper.game['url'])
print("Image: " + scraper.game['image'])
print("Title: " + scraper.game['title'])
print("Description: " + scraper.game['description'])
print("Platform: " + scraper.game['platform'])
print("Publisher: " + scraper.game['publisher'])
print("Release Date: " + scraper.game['release_date'])
print("Critic Score: " + scraper.game['critic_score'] + "/" + scraper.game['critic_outof'] + " (" + scraper.game['critic_count'] + " critics)")
print("User Score: " + scraper.game['user_score'] + " (" + scraper.game['user_count'] + " users)")
print("Developer: " + scraper.game['developer'])
print("Genre: " + scraper.game['genre'])
print("Rating: " + scraper.game['rating'])
print("Time to scrape: ", round(elapsed_time, 2), "secs")
```
* Result   
```
URL: https://www.metacritic.com/game/pc/horizon-zero-dawn-complete-edition?ref=hp  
Image: https://static.metacritic.com/images/products/games/8/5410c3d455b9c0341ef7a3023f0e29e4-98.jpg  
Title: Horizon Zero Dawn: Complete Edition  
Description: Experience Aloy’s legendary quest to unravel the mysteries of a future Earth ruled by Machines. An outcast from her tribe, the young hunter fights to uncover her past, discover her destiny… and stop a catastrophic threat to the future. Use devastating tactical attacks against your prey and explore a majestic open world in this action RPG.  
Platform: PC  
Publisher: PlayStation Mobile Inc.  
Release Date: Aug  7, 2020  
Critic Score: 85/ (41 critics)  
User Score: 4.9 (192 users)  
Developer: Guerrilla  
Genre: Role-Playing  
Rating: T  
```
