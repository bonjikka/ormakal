from bs4 import BeautifulSoup

import urllib.request
import sys
import re

fp = urllib.request.urlopen(sys.argv[1])
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, "html.parser")


table_rows = soup.find_all("tr")
for row in table_rows:
    tds = row.findChildren(recursive=False)
    # Check if first col is year
    if re.match(r"\d{4}", tds[0].get_text().strip()) :
        # stop at 2020
        if tds[0].get_text().strip() == "2020":
            break
        line=""
        for col in tds:
            line+=str(col.get_text().strip()) + ","
        print(line)

