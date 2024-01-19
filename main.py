#ლუკა ანდრიაძე
import requests
import csv
from bs4 import BeautifulSoup

# CSV column names
columns = ['number', 'name', 'year', 'platform', 'score', 'votes']

with open('games.csv', 'a', encoding='utf-8', newline='') as csvfile: #რადეგან ფაილი გახსნილიყო games.csvში,'w' კი ნიშნავს write
    csvwriter = csv.writer(csvfile)#writer ნიშნავს რომ ტექტსი ჩაიწეროს csvfileshi
    csvwriter.writerow(columns)#writerow ნიშნავს იმას რომ ფაილში ტექსტი ჩაიწეროს რიგების სახით

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = 'https://steam250.com/top250'#ეს საიტის ლინკია
response = requests.get(url, headers=headers)#ეს აგზავნის requests
soup = BeautifulSoup(response.text, 'html.parser')
games = soup.find_all('div', class_="appline")#ეს კი ყველა თამაშის კლასია

for number, game in enumerate(games, start=1):
    name = game.find('span', class_="title").text
    year = game.find('span', class_="date").text
    score = game.find('span', class_="score").text
    votes = game.find('span', class_="votes").text
    platform = game.find('span', class_="platforms").text

    # Appending data to CSV file
    with open('games.csv', 'a', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([number, name, year, platform, score, votes])

print(f"Done writing {len(games)} entries to games.csv")
