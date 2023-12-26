import json
import pandas as pd
with open("TotalStats.json") as f:
    jsondata = json.load(f)

player_info=jsondata['resultSet']['rowSet']
columns_list=[
    #"SEASON_ID"
      "PLAYER_ID",
      "RANK",
      "PLAYER",
      "TEAM_ID",
      "TEAM",
      "GP",
      "MIN",
      "FGM",
      "FGA",
      "FG_PCT",
      "FG3M",
      "FG3A",
      "FG3_PCT",
      "FTM",
      "FTA",
      "FT_PCT",
      "OREB",
      "DREB",
      "REB",
      "AST",
      "STL",
      "BLK",
      "TOV",
      "PF",
      "PTS",
      "EFF",
      "AST_TOV",
      "STL_TOV"
    ]
nba_df=pd.DataFrame(player_info,columns=columns_list)
nba_df.to_csv('trad_stats_2023-24.csv',index=False)
seasons_list = [f"{year}-{str(year + 1)[-2:]}" for year in range(1991, 2023)]
print(seasons_list)
