import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sample_data = "http://py4e-data.dr-chuck.net/comments_42.xml"
actual_data = "http://py4e-data.dr-chuck.net/comments_48984.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(actual_data, context=ctx).read()
# print(data)
tree = ET.fromstring(data)

counts = tree.findall(".//count")
sum_count = 0

# print(counts[0].text)
for count in counts:
    sum_count += int(count.text)

print(sum_count)