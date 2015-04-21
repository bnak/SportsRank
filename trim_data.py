from sys import argv
import re

'''Script to trim csv file to build directed graph from a subset of teams (single division or conference)
Writes relevant games to a new file
Used to create smaller example of just Central division in NBA'''

def trim_data(my_file, output):

    f = open(my_file)
    filetext = f.readlines()

    f.close()

    filetext = filetext[2:]
    """Filetext has game data in following format:
    Date,,Visitor/Neutral,PTS,Home/Neutral,PTS,,Notes """

    output = open(output, "w")

    for line in filetext: 
        gameData = line.split(',')
        if gameData[2] in ["Indiana Pacers", "Milwaukee Bucks","Chicago Bulls", "Cleveland Cavaliers", "Detroit Pistons"]:
            if gameData[4] in ["Indiana Pacers", "Milwaukee Bucks","Chicago Bulls", "Cleveland Cavaliers", "Detroit Pistons"]:
                output.write(line)
                print line
        else:
            pass

    output.close()
    
    return "ran"

def main(): 
    script, f1, f2 = argv
    print trim_data(f1, f2)

if __name__ == '__main__':
    main()