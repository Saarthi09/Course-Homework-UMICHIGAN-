import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')
total = 0
for span in spans:
    numb = int(span.text)
    total = total + numb
print(total)