##Web scraping  is the extraction and collection of data from websites and storing it in local machine or db
# We will use request and beautifulsoup to scrape data 

import requests
from bs4 import BeautifulSoup

#declare variable for the website to scrape data
url = 'https://archive.ics.uci.edu/ml/datasets'

#method to fetch data
response = requests.get(url)
content = response.content # gets all the content from the website

soup = BeautifulSoup(content, 'html.parser') #parse using beautifulsoup

print(soup.title)
print(soup.title.get_text)
print(soup.body)


#check status of the url  200 means 'OK'
status = response.status_code
print(status)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]

table.find('tr').find_all('td')
print(td.text)