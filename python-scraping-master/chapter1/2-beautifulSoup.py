
import sys
from bs4 import BeautifulSoup
if sys.version_info[0] == 2:
    print('version 2')
    #from urllib2 import urlopen  # Python 2
else:
    from urllib.request import urlopen #python3

html = urlopen('http://www.pythonscraping.com/exercises/exercise1.html')
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
print(bsObj.prettify())