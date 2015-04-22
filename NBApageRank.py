#Beth Nakamura, Math 462, April 2015

from sys import argv
import re
import random
import pprint
import numpy as np
from scipy import linalg

class Node(object):
    def __init__(self, name):
        self.name = name
        self.losses = {} #Key = other team, value = sum margin of losses (point differential)

    def add_loss(self, oTeam, pointDiff):
        self.losses[oTeam] = self.losses.get(oTeam, 0) + pointDiff
        #Either adds a new loss, or updates the overall pointDiff

def load_data(my_file):
    """Reads input file and creates nodes. Check that indicies align with data; 
    filename is read in as an argument from terminal (see main() function)
    INPUT: my_file - raw csv data of games
    OUTPUT: games - array of games in format games[i] = [loser, winner, pointDiff]"""
    f = open(my_file)
    filetext = f.readlines()
    f.close()
    filetext = filetext[2:] #eliminate header lines
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
    '''Processes all games and create each team as a node object
    INPUT: games - array of games in format games[i] = [loser, winner, pointDiff]
    OUTPUT: nodes - with nodes['team name'] = object node of team '''
    nodes = {} #dictionary Team Name : Team Object
    for item in games: 
        loser = item[0]
        winner = item[1]
        pointDiff = item[2]
        nodes[loser]= nodes.get(loser, Node(loser))
        nodes[loser].add_loss(winner, pointDiff)
    return nodes

def build_matrix(nodes):
    '''Builds the point differential matrix from nodes
    INPUT:
        nodes - with nodes['team name'] = object node of team 
    OUTPUT: 
        team_index - team_index['team name'] = index corresponding to row & column in A
        A - point differential matrix with A[row][column]
            Rows are losers, and entries are the point differential between column team
    '''
    A = [[0 for x in range(len(nodes.keys()))] for x in range(len(nodes.keys()))] 
    teams = sorted(nodes.keys()) #array of teams alphabetically
    team_index = {}

    for i in range(len(teams)): 
        team_index[teams[i]] = i

    for i in range(len(teams)):
        node = nodes[teams[i]]
        for item in node.losses.keys(): 
            pointDiff = node.losses[item]
            col_index = team_index[item]
            A[i][col_index] = float(pointDiff)
    return A, team_index

def markovMatrix(matrixA):
    '''Creates Markov matrix by dividing each entry in A by the sum of the row
    INPUT: A - point differential matrix with A[row][column]
            Rows are losers, and entries are the point differential between col team
    OUTPUT: H - Markov matrix
    '''
    A = np.array(matrixA)
    H = [[0 for x in range(len(A))] for x in range(len(A))] 
    for i in range(len(A)):
        row_sum = np.sum(A[i])
        for j in range(len(A[i])):
            H[i][j] = float(A[i][j])/row_sum
    return H

def pageRank(matrixA):
    '''Returns the left eigenvector (the PageRank vector) of the input matrix
    INPUT: H - Markov matrix
    OUTPUT: vl - left eigenvector, or the PageRank vector
    '''
    A = np.array(matrixA)
    H = markovMatrix(A)
    w, vl, vr = linalg.eig(H, left = True)
    vl = np.absolute(vl[:,0].T)
    return vl

def printResults(vl, team_index):
    '''Uses the team_index dictionary to interpret the results from the PageRank vector
    INPUT: 
        vl - left eigenvector, or the PageRank vector
        team_index - team_index['team name'] = index corresponding to row & column in A
    OUTPUT: 
        top10: arrray of top10 teams based on PageRank vector
    '''
    top10= []
    teams = sorted(team_index.keys())
    for i in range(10):
        ind = np.argmax(vl)
        top10.append(teams[ind])
        vl[ind] = 0
    return top10


def main():
    script, file1 = argv
    nodes = build_graph(load_data(file1))
    A, team_index =  build_matrix(nodes)
    pi = pageRank(A)
    pprint.pprint(pi)
    pprint.pprint(printResults(pi, team_index))

if __name__ == '__main__':
    main()