__author__ = 'Per'

from Match_class import Match
from Player_class import Player


numberOfPlayers = input("how many players? ")



def defPlayers():
    listOfPlayers = []
    for i in range (0, numberOfPlayers):
        playerName = str(input("Player name: "))
        matchToAssingToPlayer = Match(i)
        player_i = Player(playerName, i, matchToAssingToPlayer)
        listOfPlayers.append(player_i)