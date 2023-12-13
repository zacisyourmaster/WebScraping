import json
from pprint import pprint

with open("scores.json") as f:
    jsondata = json.load(f)

# print(jsondata["scoreboard"])
# pprint(jsondata["scoreboard"])
# dict_keys(['gameId', 'gameCode', 'gameStatus', 'gameStatusText', 'period', 'gameClock',
# 'gameTimeUTC', 'gameEt', 'regulationPeriods', 'ifNecessary',
# 'seriesGameNumber', 'seriesText', 'seriesConference',
# 'poRoundDesc', 'gameSubtype', 'homeTeam', 'awayTeam', 'gameLeaders', 'pbOdds'])

# period = jsondata["scoreboard"]["games"][0]["period"]
# gameStatus = jsondata["scoreboard"]["games"][0]["gameStatusText"]
# homeCity = jsondata["scoreboard"]["games"][0]["homeTeam"]["teamCity"]
# awayCity = jsondata["scoreboard"]["games"][0]["awayTeam"]["teamCity"]
# homeTeam = homeCity + " " + jsondata["scoreboard"]["games"][0]["homeTeam"]["teamName"]
# awayTeam = awayCity + " " + jsondata["scoreboard"]["games"][0]["awayTeam"]["teamName"]

# homeScore = jsondata["scoreboard"]["games"][0]["homeTeam"]["score"]
# awayScore = jsondata["scoreboard"]["games"][0]["awayTeam"]["score"]
# print(gameStatus,"|",homeTeam, homeScore, " - ", awayScore, awayTeam)

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
            if self.points > 29 or (self.points > 20 and (self.rebounds > 8 or self.assists > 8)):
                return 5
            else:
                return 4

    def generate_report(self, team_name):
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

        return f"{team_name} {pos[self.position]} {message}" \
               f" with {self.points} points, {self.rebounds} rebounds, "\
               f"and {self.assists} assists."


pos = {
    "PG": "Point Guard",
    "SG": "Shooting Guard",
    "SF": "Small Forward",
    "PF": "Power Forward",
    "C": "Center"
}

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
        assists=homeLeaders["assists"]
    )

    awayPlayerPerformance = PlayerPerformance(
        name=awayLeaders["name"],
        position=awayLeaders["position"],
        points=awayLeaders["points"],
        rebounds=awayLeaders["rebounds"],
        assists=awayLeaders["assists"])

    home_output_string = homePlayerPerformance.generate_report(homeTeam)
    away_output_string = awayPlayerPerformance.generate_report(awayTeam)

    print(gameStatus, "|", homeTeam, homeScore, " - ", awayScore, awayTeam)
    print(home_output_string)
    print(away_output_string)

# sample_homeLeaders = {
#     "name": "Sample Player",
#     "position": "C",  # Set the position to a valid value from your 'pos' dictionary
#     "points": 20,
#     "rebounds": 10,
#     "assists": 5
# }

# sample_awayLeaders = {
#     "name": "Another Player",
#     "position": "PG",  # Set the position to a valid value from your 'pos' dictionary
#     "points": 15,
#     "rebounds": 8,
#     "assists": 7
# }

# # Now, you can use these sample data to test your function:

# homePlayerPerformance = PlayerPerformance(
#     name=sample_homeLeaders["name"],
#     position=sample_homeLeaders["position"],
#     points=sample_homeLeaders["points"],
#     rebounds=sample_homeLeaders["rebounds"],
#     assists=sample_homeLeaders["assists"]
# )

# awayPlayerPerformance = PlayerPerformance(
#     name=sample_awayLeaders["name"],
#     position=sample_awayLeaders["position"],
#     points=sample_awayLeaders["points"],
#     rebounds=sample_awayLeaders["rebounds"],
#     assists=sample_awayLeaders["assists"]
# )

# # Call generate_report method to test the function
# home_output_string = homePlayerPerformance.generate_report("Home Team")
# away_output_string = awayPlayerPerformance.generate_report("Away Team")

# # Print the generated strings
# print(home_output_string)
# print(away_output_string)