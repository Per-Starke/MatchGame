__author__ = 'Per'

from Match_class import Match
from Player_class import Player


numberOfPlayers = input("how many players? ")



def defListOfPlayers():
    listOfPlayers = []
    for i in range (0, numberOfPlayers):
        playerName = raw_input("Player name: ")
        matchToAssingToPlayer = Match(i)
        player_i = Player(playerName, i, matchToAssingToPlayer)
        listOfPlayers.append(player_i)
    return listOfPlayers



listOfPlayers = defListOfPlayers()
for player in listOfPlayers:
    print(player.getName(), player.getNumber())


