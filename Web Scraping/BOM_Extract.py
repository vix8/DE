from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW'

html_text = requests.get(url)

soup = BeautifulSoup(html_text.text, 'html.parser')

bom = soup.find_all('div', class_ = 'a-section imdb-scroll-table-inner')

Rank = []
rank_container = soup.find_all('td', class_ = 'a-text-right mojo-header-column mojo-truncate mojo-field-type-rank')
for a in rank_container:
    Rank.append(a.text)

Movie = []
movie_container = soup.find_all('td', class_ = 'a-text-left mojo-field-type-title')
for a in movie_container:
    Movie.append(a.text)

Gross = []
gross_container = soup.find_all('td', class_ = 'a-text-right mojo-field-type-money')
for a in gross_container:
    Gross.append(a.text)

Year = []
year_container = soup.find_all('td', class_ = 'a-text-left mojo-field-type-year')
for a in year_container:
    Year.append(a.text)


df = pd.DataFrame({'Rank': Rank, 'Movie': Movie, 'Gross': Gross, 'Year': Year})

df.to_csv('Top Grossing of All Time.csv', index=False)