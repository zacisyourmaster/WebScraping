import requests
import pandas as pd

headers = {}

columns_list = [
    "PLAYER_ID", "RANK", "PLAYER", "TEAM_ID", "TEAM", "GP", "MIN", "FGM", "FGA", "FG_PCT",
    "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST", "STL",
    "BLK", "TOV", "PF", "PTS", "EFF", "AST_TOV", "STL_TOV"
]

seasons_list = [f"{year}-{str(year + 1)[-2:]}" for year in range(1991, 2023)]
dfs = []

for season_id in seasons_list:
    player_info_url = f'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season={season_id}&SeasonType=Regular%20Season&StatCategory=PTS'
    response = requests.get(url=player_info_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Attempt to parse the response as JSON
            data = response.json()
            player_info = data['resultSet']['rowSet']
            df = pd.DataFrame(player_info, columns=columns_list)
            df['season_id'] = season_id
            print(season_id)
            dfs.append(df)
        except Exception as e:
            print(f"Error parsing JSON for season {season_id}: {e}")
    else:
        print(f"Request failed for season {season_id} with status code {response.status_code}")

final_df = pd.concat(dfs, sort=False)
final_df.to_csv('trad_stats_1993-2023.csv')
