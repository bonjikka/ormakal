from bs4 import BeautifulSoup

import urllib.request
import sys

fp = urllib.request.urlopen(sys.argv[1])
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, "html.parser")

movie_category = soup.find("div",class_="filmo-category-section")
movie_names = movie_category.find_all("div",class_="filmo-row")
# print(movie_names)
for movie_name in movie_names:
    year=movie_name.find("span").get_text().strip()
    name=movie_name.find("a").get_text().strip()
    text_list=movie_name.findAll(text=True, recursive=False)
    charcter_name= text_list[3].strip() if len(text_list)==4 else ""
    print(f"{year},{name},{charcter_name}")
