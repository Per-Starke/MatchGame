__author__ = 'Per'

from Match_class import Match
from Player_class import Player


numberOfPlayers = input("how many players? ")



def defineListOfPlayers():
    listOfPlayers = []
    for i in range (0, numberOfPlayers):
        playerName = raw_input("Player name: ")
        matchToAssingToPlayer = Match(i)
        player_i = Player(playerName, i, matchToAssingToPlayer)
        listOfPlayers.append(player_i)
    return listOfPlayers

def defineListOfMatches():
    listOfMatches = []
    for i in range (0, numberOfPlayers):
        match = player.getAssignedMatch
        listOfMatches.append(match)
    return listOfMatches

listOfMatches = defineListOfMatches()
for match in listOfMatches:
        print("Match Nr: ", match.getNumber(), "Match length: ", match.getLength())


listOfPlayers = defineListOfPlayers()
for player in listOfPlayers:
    print(player.getName(), player.getNumber())


