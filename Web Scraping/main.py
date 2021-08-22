from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.imdb.com/chart/toptv/').text

soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find('td','titleColumn').text.replace('      ', '').replace('\n' , ' ').strip()
rating = soup.find('td', class_ = 'ratingColumn imdbRating').text

print(movies)
print(rating)
