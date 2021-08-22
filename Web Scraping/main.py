from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW').text

soup = BeautifulSoup(html_text, 'lxml')

rank = soup.find('td','a-text-right mojo-header-column mojo-truncate mojo-field-type-rank').text
movies = soup.find('td','a-text-left mojo-field-type-title').text
gross = soup.find('td', class_ = 'a-text-right mojo-field-type-money').text
year = soup.find('td','a-text-left mojo-field-type-year').text

print(rank)
print(movies)
print(gross)
print(year)