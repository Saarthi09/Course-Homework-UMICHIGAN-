import json
import urllib
import urllib.request

URL = input("Enter URL: ")
print("Retrieving ", URL)
uh = urllib.request.urlopen(URL)
data = uh.read().decode()
js = json.loads(data)
total = 0
user_count = len(js["comments"])
print("User Count: " , user_count)
for item in js["comments"]:
    number = item['count']
    numb = int(number)
    total = total + numb
print (total)

#test url: http://py4e-data.dr-chuck.net/comments_42.json
#assignment url: http://py4e-data.dr-chuck.net/comments_2155539.json