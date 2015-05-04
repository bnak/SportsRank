# SportsRank
##PageRank and Sports Teams

To run from terminal: ```python NBApageRank.py 'nba1415.csv'```

See [report](https://www.dropbox.com/s/orekk7ycoc2z5y8/SportsRank.pdf?dl=0) about PageRank background and model results.

Datasets are from http://www.basketball-reference.com/ and http://www.hockey-reference.com/

Google’s [PageRank algorithm](http://en.wikipedia.org/wiki/PageRank) allows efficient ranking of webpages by creating a directed graph of the web. By considering each webpage a node and hyperlinks as the arcs, the resulting Markov matrix provides the left steady-state eigenvector; this PageRank vector provides the relative probabilities each webpage, and thus a ranking. PageRank provides a ranking of a complex network using a single measure, the number and direction of hyperlinks. SportsRank applies this model to athletics, demonstrated here with the NBA. This model examines whether there is a better way of ranking sports compared to the standard win-loss method of ranking.

We consider each team as a node, with the arc from node i to node j carrying the value of the total amount team i lost to team j over all games played in a season. 

###Example: NBA Central Division, 2013-2014 Season

As an example, we’ll apply this model to a smaller subset of teams, specifically the Central Division consisting of the following five teams: Chicago Bulls, Cleveland Cavaliers, Detroit Pistons, Indiana Pacers, and Milwaukee Bucks. In the 2013-2014 season, these five teams played forty inter-divisional games; the point differentials of these games create a closed directed graph shown below. Recall that the value of the arcs is the sum total the team lost to next team overall games played – i.e., over all the games between the Milwaukee Bucks and the Indiana Pacers, Milwaukee’s point differential in losses totaled 44 points; Indiana never lost to Milwaukee. 


![alt text](https://github.com/bnak/SportsRank/blob/master/directedgraph.png "Central Division Directed Graph")



This directed graph is then converted to a point differential matrix; entries are then divided by the sum of each row to create a stochastic Markov matrix. 




![alt text](https://github.com/bnak/SportsRank/blob/master/matrix.png "Matrix")



![alt text](https://github.com/bnak/SportsRank/blob/master/results.png "Results")



There are discrepancies between the two rankings, which is expecting considering the different data sets (Actual Season Rankings uses all games played, whereas this example only uses the forty inter-divisional games).  The limited dataset provides insight on the differences in the rankings. The Chicago Bulls are ranked higher than the Indiana Pacers in the model because over the four games they played each other, they split the series 2-2 with point differentials of 29 and 28 points, respectively, whereas Indiana won more games overall during the regular season. Similarly, the Cavaliers performed relatively poorly within the division, losing over half the games, resulting in a lower rank when considering only inter-divisional games. 


###Background Research and Sources: 

[Ranking National Football League Teams Using Google’s PageRank, by Angela Y. Govan and Carl D. Meyer](http://www.ncsu.edu/crsc/reports/ftp/pdf/crsc-tr06-19.pdf)

[PageRank Beyond the Web, by David F. Gleich](http://arxiv.org/pdf/1407.5107v1.pdf)

[The predictive power of ranking systems in association football, by Jan Lasek, Zotan Szlavik, and Sandjai Bhulai](http://www.few.vu.nl/~zszlavik/papers/IJAPR.pdf)

[Markov Chains, Google’s PageRank Algorithm, by Jeff Jauregui, UPenn Math Slidedeck](http://www.math.upenn.edu/~kazdan/312F12/JJ/MarkovChains/markov_google.pdf)

[The PageRank Citation Ranking: Bringing Order to the Web by Larry Page, Sergey Brin, et al.](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)


