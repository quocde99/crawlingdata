from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# dic include column in raw data
d = {'name': [], 'price': []}
# name column
nameind = ["name", "price"]
# tag
tag = ["div", "div"]
# class name in tag html
listClass = ["name", "price-discount__price"]
# page
page = 1
while page < 5:
    with urlopen('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?page='+str(page)+'&src=c.1789.hamburger_menu_fly_out_banner') as response:
        print('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?page='+str(page)+'&src=c.1789.hamburger_menu_fly_out_banner')
        soup = BeautifulSoup(response, 'html.parser')
        n = 0
        while n < len(nameind):
            for anchor in soup.find_all(tag[n], class_=listClass[n]):
                text = anchor.text.strip()
                d[nameind[n]].append(text)
            n = n + 1
    page = page + 1
df = pd.DataFrame(data=d)
print(df)
df.to_csv("E:\\FPT\\output.csv", encoding='utf-8-sig')