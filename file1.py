from bs4 import BeautifulSoup
import requests

url = 'https://www.billboard.com/charts/hot-100'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

allSongs = soup.findAll("div", {"class":"chart-list-item"})
no1 = soup.find("div", {"class":"chart-number-one__title"}).text.strip()
no1artist = soup.find("div",{"class" : "chart-number-one__artist"}).a.text.strip()
print(no1)
print(no1artist)
print()

#print(allSongs[1])

# name = allSongs[0].find("div", {"class":"chart-list-item__title"}).span.text.strip()
# artist = song.find("div", {"class":"chart-list-item__artist"}).a.text.strip()
# lyrics_url = song.find("div", {"class":"chart-list-item__lyrics"}).a["href"]


for song in allSongs:
    name = song["data-artist"]
    artist = song["data-title"]
    rank = song["data-rank"]

    if song.find("div", {"class":"chart-list-item__lyrics"}) != None:
        lyrics_url = song.find("div", {"class":"chart-list-item__lyrics"}).a["href"]

    print(rank)
    print(name)
    print(artist)
    print(lyrics_url)
    print()


#chart-list-item__lyrics
