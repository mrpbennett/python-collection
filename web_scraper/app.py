import os
import requests
from bs4 import BeautifulSoup

# from dotenv import load_dotenv
# load_dotenv()

url = "https://www.google.co.uk/finance"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", {"class": "UDZeY"})

print(results)
