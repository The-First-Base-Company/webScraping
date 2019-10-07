class Team: 

    def __init__(self, teamID, name, conference, division, rank, wins, losses, location):
        self.teamID = teamID
        self.name = name
        self.conference = conference
        self.division = division
        self.rank = rank
        self.wins = wins
        self.losses = losses
        self.location = location

    def getID(self):
        return teamID

    def getName(self):
        return name
    def getConference(self):
        return conference
    def getDivision(self):
        return division
    def getRank(self):
        return rank
    def getWins(self):
        return wins
    def getLosses(self):
        return losses
    def getLocation(self):
        return location