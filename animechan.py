from urllib.request import urlopen
import ssl
import json

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

JS = urlopen('https://animechan.vercel.app/api/random', context=ctx).read()
js = json.loads(JS)

# print(js['quote'])
# print('  ~~  ' + js['character'] + ' from ' + js['anime'])