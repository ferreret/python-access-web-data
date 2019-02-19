# Sample url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Data url: http://py4e-data.dr-chuck.net/known_by_Amylea.html


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/known_by_Amylea.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

count = 0

while count < 6:    
    url = tags[17].get("href", None)
    # print(url)
    print(tags[17].text)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')        
    # print(tags[2].text)
    count += 1

print(tags[17].text)
# for tag in tags:
#     print(tag.get('href', None))