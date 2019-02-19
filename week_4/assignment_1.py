# Sample data: http://py4e-data.dr-chuck.net/comments_42.html
# Actual data:  http://py4e-data.dr-chuck.net/comments_48982.html


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_48982.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
spans = soup("span")

span_values = list()
for span in spans:
    span_values.append(int(span.text))

print(sum(span_values))
