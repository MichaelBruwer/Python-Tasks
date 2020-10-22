import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.takealot.com/raidmax-dk925-argb-gaming-chair/PLID70475671")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "currency plus currency-module_currency_29IIm"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = (float(price_without_symbol))

if price < 200:
    print("buy chair")
else:
    print("dont buy")

# <span class="currency plus currency-module_currency_29IIm">R 3,195</span>

