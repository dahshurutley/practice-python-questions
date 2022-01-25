# Use the BeautifulSoup and requests Python packages
# Print out a list of all the article titles on the New York Times
# Due to the formating of the website, Other less important title will be...
# Included within the output (Such as 'Spelling Bee' or 'The Crossword')

import requests 
from bs4 import BeautifulSoup
from lxml import html

# Note: Use soup.get-all-text to return all text from the article

url = 'http://www.nytimes.com/'
r = requests.get(url)
# Personal Note: r.text displays the websites HTML
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
# For loop finds each h3 value and gets text from each said value/class. 
for i in soup.find_all("h3", {"class": "e1lsht870"}):
    
    print(i.getText())


    



