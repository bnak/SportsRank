#!/usr/bin/env python

from sys import argv
import re
import random
import pprint
#script, filename = argv

class Node(object):
    def __init__(self, name):
        self.name = name
        self.losses = {}

    def add_loss(self, oTeam, pointDiff):
        self.losses[oTeam] = self.losses.get(oTeam, 0) + pointDiff

def load_data(my_file):
    """Reads input file and creates nodes."""

    f = open(my_file)
    filetext = f.readlines()


    f.close()

    filetext = filetext[2:]
    """Filetext has game data in following format:
    Date,,Visitor/Neutral,PTS,Home/Neutral,PTS,,Notes """
    games = []


    for line in filetext: 
        gameData = line.split(',')
        if int(gameData[3]) < int(gameData[5]):
            loser = gameData[2]
            winner = gameData[4]
            pointDiff = int(gameData[5]) - int(gameData[3])

        else: 
            winner = gameData[2]
            loser = gameData[4]
            pointDiff = int(gameData[3]) - int(gameData[5])
            
        games.append([loser, winner, pointDiff])

    
    return games

def build_graph(games):
    nodes = {} #dictionary Team Name : Team Object
    for item in games: 
        loser = item[0]
        winner = item[1]
        pointDiff = item[2]

        nodes[loser]= nodes.get(loser, Node(loser))
        nodes[loser].add_loss(winner, pointDiff)

    return nodes

def build_matrix(nodes):

def main():


    script, file1 = argv
    nodes = build_graph(load_data(file1))
    pprint.pprint(nodes['Milwaukee Bucks'].losses)
    print len(nodes['Utah Jazz'].losses)
    print len(nodes['Milwaukee Bucks'].losses)


if __name__ == '__main__':
    main()