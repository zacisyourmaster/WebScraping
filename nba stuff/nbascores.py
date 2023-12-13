# from bs4 import BeautifulSoup
# import requests




# url="https://www.basketball-reference.com/boxscores/"
# result=requests.get(url)
# soup=BeautifulSoup(result.text,'html.parser')
# game_summaries = soup.find_all("div", class_="game_summary expanded nohover")
# scores=""
# for score in game_summaries:
# 	loser= score.find("tr", class_="loser").text.strip()
# 	winner= score.find("tr", class_="winner").text.strip()

# 	lInfo=loser.split('\n')
# 	wInfo=winner.split('\n')
# 	scores+=wInfo[0]+" defeated "+lInfo[0]+" "+wInfo[1]+" to "+lInfo[1]+"\n-----------------------------------\n"
from bs4 import BeautifulSoup
import requests
from plyer import notification

url = "https://www.basketball-reference.com/boxscores/"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
game_summaries = soup.find_all("div", class_="game_summary expanded nohover")
scores = []

for score in game_summaries:
    loser = score.find("tr", class_="loser").text.strip()
    winner = score.find("tr", class_="winner").text.strip()

    lInfo = loser.split('\n')
    wInfo = winner.split('\n')
    game_summary = f"{wInfo[0]} defeated {lInfo[0]} {wInfo[1]} to {lInfo[1]}"
    scores.append(game_summary)

# Create a big notification in the middle of the screen
notification_title = "Basketball Scores Update"
notification_text = "\n".join(scores[:5])  # Displaying the first 5 game summaries
notification_app_name = "Basketball Scores App"

notification.notify(
    title=notification_title,
    message=notification_text,
    app_name=notification_app_name,
    timeout=10,  # Timeout in seconds
    toast=False  # To create a big notification in the middle of the screen
)