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

def defineListOfMatches(listOfPlayers):

    listOfMatches = []

    for player in listOfPlayers:
        match = player.getAssignedMatch()
        listOfMatches.append(match)

    return listOfMatches


listOfPlayers = defineListOfPlayers()

listOfMatches = defineListOfMatches(listOfPlayers)


for player in listOfPlayers:
    match = player.getAssignedMatch()
    matchNr = match.getNumber()
    matchLength = match.getLength()

    print("Player name: ", player.getName(), "Player Nr: ", player.getNumber())
    print("Match Nr: ", matchNr, "Match length: ", matchLength)
    print("")


print("")
print(listOfMatches)
print("")
print(listOfPlayers)