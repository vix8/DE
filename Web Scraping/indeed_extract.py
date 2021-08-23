from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://in.indeed.com/jobs?q=Data+Engineer&l=Bengaluru').text

soup = BeautifulSoup(html_text, 'lxml')

