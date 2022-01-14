from urllib.request import urlopen
import ssl
import json
import textwrap


# Ignoring SSL (Secure Sockets Layer) certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

JS = urlopen('https://animechan.vercel.app/api/random', context=ctx).read()
js = json.loads(JS)

## API https://animechan.vercel.app/ by https://www.rocktimcodes.site/ !!!! GO SUPPORT!!!!!

# print(js['quote'])
# print('  ~~  ' + js['character'] + ' from ' + js['anime'])

quote = textwrap.wrap(js['quote'])
by = ' ~~  ' + js['character'] + ', from ' + js['anime']