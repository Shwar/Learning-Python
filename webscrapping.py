##Web scraping  is the extraction and collection of data from websites and storing it in local machine or db
# We will use request and beautifulsoup to scrape data 
'''
import requests
from bs4 import BeautifulSoup

#declare variable for the website to scrape data
url = 'https://en.wikipedia.org/wiki/IBM'

#method to fetch data
response = requests.get(url)
content = response.content # gets all the content from the website
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser') #parse using beautifulsoup

print(html_content[:500])
#check status of the url  200 means 'OK'
status = response.status_code
print(status)
print(html_content.title)

links = soup.find_all('a')
for link in links:
    print(link.text)

'''
#Using pandas to scrape data
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(url)
df = tables[0]
print(df)

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(URL)
df1 = tables[2] # the required table will have index 2
print(df1)