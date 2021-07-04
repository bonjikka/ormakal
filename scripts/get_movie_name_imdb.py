from bs4 import BeautifulSoup

import urllib.request
import sys

fp = urllib.request.urlopen(sys.argv[1])
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, "html.parser")


# Each movie block has following format
# 
# <h3 class="lister-item-header">
# <span class="lister-item-index unbold text-primary">100.</span>
# <a href="/title/tt1745863/">Urumi</a>
# <span class="lister-item-year text-muted unbold">(2011)</span>
# </h3>


movie_names = soup.find_all("h3",class_="lister-item-header")
for title_element in movie_names:
    title = title_element.find("a").get_text()
    year = title_element.find("span", class_="text-muted").get_text()
    print(f"{title}, {year}")
