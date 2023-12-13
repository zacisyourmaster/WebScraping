from bs4 import BeautifulSoup
import requests
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

gpu=input("What are you searching for? ")

url=f"https://www.newegg.com/p/pl?d={gpu}"
page=requests.get(url).text
doc=BeautifulSoup(page,"html.parser")

page_text=doc.find(class_="list-tool-pagination-text")
print(page_text)