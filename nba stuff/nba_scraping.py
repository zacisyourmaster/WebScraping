from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import sys

import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')

url="https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
result=requests.get(url).text
soup=BeautifulSoup(result,"html.parser")
table=soup.find('table', class_="stats_table")
#print(table)
stat_titles=table.find_all('th')
tableTitles=[title.text for title in stat_titles] 
tableTitles=tableTitles[:30]
#print(tableTitles)
df= pd.DataFrame(columns=tableTitles)
column_data=table.find_all('tr')
seen_nums=set()
num=1
for row in column_data:
    rank_tag=row.find('th')
    
    if rank_tag and not rank_tag.text.strip().isdigit():
        continue
    
    rank = rank_tag.text.strip() if rank_tag else "N/A"
    if rank in seen_nums:
        continue
    row_data=row.find_all('td')
    ind_row_data=[num] + [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length]=ind_row_data
    num+=1
    
#df.to_csv(r"Players.csv", index=False)
# df.to_excel("Players.xlsx")
# df.to_json("2024Players.json")


