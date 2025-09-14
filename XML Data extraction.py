import urllib.request 
import xml.etree.ElementTree as ET
url = input("Enter url: ")
if len(url) <1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
uh = urllib.request.urlopen(url).read()
sum = 0
tree = ET.fromstring(uh)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total = total + int(count.text)
print(total)