#!/usr/bin/env python

from sys import argv
import re
import random
import pprint
from numpy import linalg 
from scipy.linalg import eig


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
    # Adjacency matrix A with A[row][column]
    # Rows are losers, and entries are the point differential between col team
    A = [[0 for x in range(30)] for x in range(30)] 
    teams = sorted(nodes.keys()) #array of teams alphabetically
    team_index = {}

    for i in range(len(teams)): 
        team_index[teams[i]] = i

    for i in range(len(teams)):
        node = nodes[teams[i]]
        for item in node.losses.keys(): 
            pointDiff = node.losses[item]
            col_index = team_index[item]
            A[i][col_index] = pointDiff

    return A

def pageRank(matrix):


def main():


    script, file1 = argv
    nodes = build_graph(load_data(file1))
    A =  build_matrix(nodes)


if __name__ == '__main__':
    main()