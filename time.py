import argparse
import json
from datetime import datetime
import random

def LoadJson():
    with open(r"C:\Users\drorm\Documents\teams.json", 'r', encoding='utf-8') as file:
        return json.load(file)
        
def ShowTeamById(TeamsJson, id):
    text = ""
    if id == -1:
        teams = []
        for team in TeamsJson:
            teams.append(team["id"])
        id = random.choice(teams)
    
    for team in TeamsJson:
        if team["id"]== id:
            last = datetime.strptime(team["last"], "%Y-%m-%d %H:%M:%S")
            now = datetime.now()
            time_diff = now - last
            text = "\nIt has been " + str(time_diff) + " since "
            text += "the " + team["team"] + " last played in the " + team["title"]
            print(text)
    if text == "":
        print ("There's no such team\nRun with -T option to see all the teams")

def ShowAllTeams(TeamsJson, league = ""):
    for team in TeamsJson:
        if ( (league == "") or
            (league.lower() == "mlb" and team["title"] == "World Series") or
            (league.lower() == "nfl" and team["title"] == "Super Bowl") or
            (league.lower() == "nhl" and team["title"] == "Stanley Cup Finals") or
            (league.lower() == "nba" and team["title"] == "NBA Finals") ) :
                print(str(team["id"]) + ": " + team["team"]) 

def SetupArgs():
    parser = argparse.ArgumentParser(description='Displays the last time a team has competed in a championship game.')
    parser.add_argument('-t', '--team-id', type=int, help='Show last championship for a specific team by ID.')
    parser.add_argument('-T', '--all-teams', action='store_true', help='List all teams.')
    parser.add_argument('-l', '--league', type=str, help='Show teams by league (MLB/NFL/NHL/NBA).')
    parser.add_argument('-r', '--random', action='store_true', help='Show a random team.')
    return parser.parse_args()

def main():
    TeamsJson = LoadJson()

    args = SetupArgs()
    if args.team_id is not None:
        ShowTeamById(TeamsJson, args.team_id)
    elif args.random is not None:
        ShowTeamById(TeamsJson, -1)
    elif args.league is not None:
        ShowAllTeams(TeamsJson, args.league)
    elif args.all_teams:
        ShowAllTeams(TeamsJson)
    else:
        # Handle case where no option is provided (optional)
        print("Please enter a valid option")

if __name__ == "__main__":
    main()
