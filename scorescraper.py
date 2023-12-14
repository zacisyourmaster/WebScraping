import datetime
import requests
import json

url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

payload = {}
headers = {
    "Cookie": "ak_bmsc=794EC46C635BA1B9F4CF7E95B46264D6~000000000000000000000000000000~YAAQSfferZGFs0iMAQAA2nKjZBbgqkhwUamOYIxr5RLKcYqFyCE6dTwKp5a/0gOt4vrB2XIuBlAqoQmC5sw0oVoHprg0J0RqDCxcoxYBCNnRLLRvWCeA5loNZgFmUbi19qLD2ZDAh9nb15Vu1MRQ40+1XPVCPnyPhWpAsLVYpPWAyguRJOXx1T96BLiLRHmaD4PkbpOdsip5zrlwggJxcQmxLOuMDYPqB+t2N+QiFp4h8q2sUPA8P+4ctvqqUe106ne55Rr7o9ONpeXcCVwuot7jJgTSMlZf7SB9d18Q0UQEWFidC0fgXHubxxOayOokwIEoqx2Npqa6/+OWvzDHPFq0FZgfwC/4tWeeHtglLgFkAq2QLUkxXQ=="
}

response = requests.request("GET", url, headers=headers, data=payload)

jsondata = json.loads(response.text)


class PlayerPerformance:
    def __init__(self, name, position, points, rebounds, assists):
        self.name = name
        self.position = position
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def calculate_rating(self):
        if self.points < 10:
            return 1
        elif 10 <= self.points <= 17:
            return 2
        elif 18 <= self.points <= 23:
            return 3
        elif 24 <= self.points <= 29:
            return 4
        else:
            if self.points > 29 or (
                self.points > 20 and (self.rebounds > 8 or self.assists > 8)
            ):
                return 5
            else:
                return 4

    def generate_report(self, team_name, positions):
        rating = self.calculate_rating()
        if rating == 1:
            message = f"{self.name} faced challenges in the game."
        elif rating == 2:
            message = f"{self.name} had a solid performance."
        elif rating == 3:
            message = f"{self.name} played well."
        elif rating == 4:
            message = f"{self.name} delivered an impressive performance."
        else:
            message = f"{self.name} gave an outstanding performance."

        return (
            f"{team_name} {pos[self.position]} {message}"
            f" with {self.points} points, {self.rebounds} rebounds, "
            f"and {self.assists} assists."
        )


pos = {
    "PG": "Point Guard",
    "SG": "Shooting Guard",
    "SF": "Small Forward",
    "PF": "Power Forward",
    "C": "Center",
}
messages = []
current_date = datetime.now().strftime("%Y-%m-%d")
messages.append(f"Hi Zach, here are game scores for {current_date}\n")
for game in jsondata["scoreboard"]["games"]:
    gameStatus = game["gameStatusText"]
    homeCity = game["homeTeam"]["teamCity"]
    awayCity = game["awayTeam"]["teamCity"]
    homeTeam = homeCity + " " + game["homeTeam"]["teamName"]
    awayTeam = awayCity + " " + game["awayTeam"]["teamName"]

    homeScore = game["homeTeam"]["score"]
    awayScore = game["awayTeam"]["score"]

    # Assuming the player performance data is available for the home and away teams
    homeLeaders = game["gameLeaders"]["homeLeaders"]
    awayLeaders = game["gameLeaders"]["awayLeaders"]

    homePlayerPerformance = PlayerPerformance(
        name=homeLeaders["name"],
        position=homeLeaders["position"],
        points=homeLeaders["points"],
        rebounds=homeLeaders["rebounds"],
        assists=homeLeaders["assists"],
    )

    awayPlayerPerformance = PlayerPerformance(
        name=awayLeaders["name"],
        position=awayLeaders["position"],
        points=awayLeaders["points"],
        rebounds=awayLeaders["rebounds"],
        assists=awayLeaders["assists"],
    )

    home_output_string = homePlayerPerformance.generate_report(homeTeam, pos)
    away_output_string = awayPlayerPerformance.generate_report(awayTeam, pos)
    game_string = f"{gameStatus} | {homeTeam} {homeScore} - {awayScore} {awayTeam}"
    messages.extend([game_string, home_output_string, away_output_string, ""])
    # print(gameStatus, "|", homeTeam, homeScore, " - ", awayScore, awayTeam)
    # print(home_output_string)
    # print(away_output_string)

messages.pop()
formatted_messages = "\n\n".join(messages)

resp = requests.post(
    "https://textbelt.com/text",
    {
        "phone": "8584428115",
        "message": formatted_messages,
        "key": "my-key",
    },
)
print(resp.json())
