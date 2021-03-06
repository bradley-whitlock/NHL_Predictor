import json

# This was scraped from NHL.com
TEAMS_ACTUAL = {"35": {"displayAbbrev": "CLR", "fullName": "Colorado Rockies", "teamId": 35},
                "36": {"displayAbbrev": "SEN", "fullName": "Ottawa Senators (1917)", "teamId": 36},
                "33": {"displayAbbrev": "WIN", "fullName": "Winnipeg Jets (1979)", "teamId": 33},
                "34": {"displayAbbrev": "HFD", "fullName": "Hartford Whalers", "teamId": 34},
                "39": {"displayAbbrev": "QUA", "fullName": "Philadelphia Quakers", "teamId": 39},
                "37": {"displayAbbrev": "HAM", "fullName": "Hamilton Tigers", "teamId": 37},
                "38": {"displayAbbrev": "PIR", "fullName": "Pittsburgh Pirates", "teamId": 38},
                "43": {"displayAbbrev": "MMR", "fullName": "Montreal Maroons", "teamId": 43},
                "42": {"displayAbbrev": "QBD", "fullName": "Quebec Bulldogs", "teamId": 42},
                "41": {"displayAbbrev": "MWN", "fullName": "Montreal Wanderers", "teamId": 41},
                "40": {"displayAbbrev": "DCG", "fullName": "Detroit Cougars", "teamId": 40},
                "22": {"displayAbbrev": "EDM", "fullName": "Edmonton Oilers", "teamId": 22},
                "23": {"displayAbbrev": "VAN", "fullName": "Vancouver Canucks", "teamId": 23},
                "24": {"displayAbbrev": "ANA", "fullName": "Anaheim Ducks", "teamId": 24},
                "25": {"displayAbbrev": "DAL", "fullName": "Dallas Stars", "teamId": 25},
                "26": {"displayAbbrev": "LAK", "fullName": "Los Angeles Kings", "teamId": 26},
                "27": {"displayAbbrev": "PHX", "fullName": "Phoenix Coyotes", "teamId": 27},
                "28": {"displayAbbrev": "SJS", "fullName": "San Jose Sharks", "teamId": 28},
                "29": {"displayAbbrev": "CBJ", "fullName": "Columbus Blue Jackets", "teamId": 29},
                "3": {"displayAbbrev": "NYR", "fullName": "New York Rangers", "teamId": 3},
                "2": {"displayAbbrev": "NYI", "fullName": "New York Islanders", "teamId": 2},
                "1": {"displayAbbrev": "NJD", "fullName": "New Jersey Devils", "teamId": 1},
                "30": {"displayAbbrev": "MIN", "fullName": "Minnesota Wild", "teamId": 30},
                "7": {"displayAbbrev": "BUF", "fullName": "Buffalo Sabres", "teamId": 7},
                "6": {"displayAbbrev": "BOS", "fullName": "Boston Bruins", "teamId": 6},
                "5": {"displayAbbrev": "PIT", "fullName": "Pittsburgh Penguins", "teamId": 5},
                "32": {"displayAbbrev": "QUE", "fullName": "Quebec Nordiques", "teamId": 32},
                "4": {"displayAbbrev": "PHI", "fullName": "Philadelphia Flyers", "teamId": 4},
                "31": {"displayAbbrev": "MNS", "fullName": "Minnesota North Stars", "teamId": 31},
                "9": {"displayAbbrev": "OTT", "fullName": "Ottawa Senators", "teamId": 9},
                "8": {"displayAbbrev": "MTL", "fullName": "Montreal Canadiens", "teamId": 8},
                "58": {"displayAbbrev": "TSP", "fullName": "Toronto St. Patricks", "teamId": 58},
                "57": {"displayAbbrev": "TAN", "fullName": "Toronto Arenas", "teamId": 57},
                "19": {"displayAbbrev": "STL", "fullName": "St. Louis Blues", "teamId": 19},
                "56": {"displayAbbrev": "CGS", "fullName": "California Golden Seals", "teamId": 56},
                "17": {"displayAbbrev": "DET", "fullName": "Detroit Red Wings", "teamId": 17},
                "18": {"displayAbbrev": "NSH", "fullName": "Nashville Predators", "teamId": 18},
                "15": {"displayAbbrev": "WSH", "fullName": "Washington Capitals", "teamId": 15},
                "16": {"displayAbbrev": "CHI", "fullName": "Chicago Blackhawks", "teamId": 16},
                "13": {"displayAbbrev": "FLA", "fullName": "Florida Panthers", "teamId": 13},
                "14": {"displayAbbrev": "TBL", "fullName": "Tampa Bay Lightning", "teamId": 14},
                "11": {"displayAbbrev": "ATL", "fullName": "Atlanta Thrashers", "teamId": 11},
                "12": {"displayAbbrev": "CAR", "fullName": "Carolina Hurricanes", "teamId": 12},
                "21": {"displayAbbrev": "COL", "fullName": "Colorado Avalanche", "teamId": 21},
                "20": {"displayAbbrev": "CGY", "fullName": "Calgary Flames", "teamId": 20},
                "49": {"displayAbbrev": "CLE", "fullName": "Cleveland Barons", "teamId": 49},
                "48": {"displayAbbrev": "KCS", "fullName": "Kansas City Scouts", "teamId": 48},
                "45": {"displayAbbrev": "SLE", "fullName": "St. Louis Eagles", "teamId": 45},
                "44": {"displayAbbrev": "NYA", "fullName": "New York Americans", "teamId": 44},
                "47": {"displayAbbrev": "AFM", "fullName": "Atlanta Flames", "teamId": 47},
                "46": {"displayAbbrev": "OAK", "fullName": "Oakland Seals", "teamId": 46},
                "10": {"displayAbbrev": "TOR", "fullName": "Toronto Maple Leafs", "teamId": 10},
                "51": {"displayAbbrev": "BRK", "fullName": "Brooklyn Americans", "teamId": 51},
                "52": {"displayAbbrev": "WPG", "fullName": "Winnipeg Jets", "teamId": 52},
                "53": {"displayAbbrev": "ARI", "fullName": "Arizona Coyotes", "teamId": 53},
                "54": {"displayAbbrev": "VGK", "fullName": "Vegas Golden Knights", "teamId": 54},
                "50": {"displayAbbrev": "DFL", "fullName": "Detroit Falcons", "teamId": 50}}


# TODO: Currently exists an error with the Montréal Canadiens where is replaces the é with antoher character.
# TODO: Current fix is to manually go in and change the é to e to match the data scraped from game_scraper
# TODO: When this JSON object is updated, go and replace the é with an e

def team_id_parser():
    dict_pair = {}
    for pair in TEAMS_ACTUAL.items():
        name = pair[1]['fullName']
        dict_pair[name] = pair[0]

    with open('data/teams/team_ids.json', 'w') as outfile:
        json.dump(dict_pair, outfile)
