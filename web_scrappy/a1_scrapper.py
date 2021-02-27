import requests

from bs4 import BeautifulSoup

URL = 'https://www.flipkart.com/asus-zenbook-14-core-i5-11th-gen-8-gb-512-gb-ssd-windows-10-home-ux425ea-bm501ts-thin-light-laptop/p/itm173bc935b2a33?pid=COMFWXWWZYFRCPW7&lid=LSTCOMFWXWWZYFRCPW7PFUQPK&marketplace=FLIPKART&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_2_15_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_15_na_na_ps&fm=SEARCH&iid=315b00e4-799f-4c3d-a655-7a30c91e063c.COMFWXWWZYFRCPW7.SEARCH&ppt=sp&ppn=sp&ssid=sge1aw261s0000001612964237995&qH=04a51f586ca0b3e6'

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            })


page = requests.get(URL, headers = HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# title = soup.find_all("div", class_="B_NuCI")

# print(title)
