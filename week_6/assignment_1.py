import urllib.request, urllib.parse, urllib.error
import json
import ssl

SAMPLE_DATA = "http://py4e-data.dr-chuck.net/comments_42.json"
ACTUAL_DATA = "http://py4e-data.dr-chuck.net/comments_48985.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(ACTUAL_DATA, context=ctx).read().decode()

info = json.loads(data)

sum_count = 0
# print(info)
comments = info["comments"]

for item in comments:
    sum_count += int(item["count"])

print(sum_count)