"""A demontration of dictionary operations"""

# A dictionary of Manchester City's players
players = {
    "Ederson" : "Goal Keeper",
    "Diaz" : "Centre Back",
    "Akanji" : "Centre Back",
    "Ake" : "Centre Back",
    "Stones": "Defensive Midfielder",
    "Rodri" : "Defensive Midfielder",
    "Bernado" : "winger",
    "Haaland" : "Striker",
}

[print(f"{pl_name} is a {pl_position}") for pl_name, pl_position in players.items()]
print()
[print(key) for key in players.keys()]
print()
[print(key) for key in sorted(players.keys())]
print()
[print(key) for key in sorted(set(players.values()))]
