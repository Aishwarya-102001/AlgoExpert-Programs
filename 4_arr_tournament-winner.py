
#*** Time --> O(n) , n = no. of competitions --> as we use for loop to traverse via the competitions array
#*** Space --> O(k) , k = no. of teams --> as we form new data structure K/A "scores" 

Home_team_won = 1
def tournamentWinner(competitions, results):
    currentBestTeam = " "
    scores = {currentBestTeam: 0}
    for idx , competition in enumerate(competitions):  #gives access to the values and index of competitions array
        result = results[idx]
        homeTeam , awayTeam = competition  #splits the array as homeTeam and awayTeam
        winningTeam = homeTeam if result == Home_team_won else awayTeam  #checks the winningTeam

        updateScores(winningTeam, 3 , scores) #updates the score of each team according to results of each competition

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam    #update the currentBestTeam if score of winning team is greater than the scores from given teams

    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] +=points
	
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"],["Java", "C"], ["HTML", "C#"]]
results = [0, 1, 1, 1, 0 ]   # 1 --> home team wins i.e first team from each competition
                             # 0 --> away team wins i.e second team from each competition

print(tournamentWinner(competitions, results))