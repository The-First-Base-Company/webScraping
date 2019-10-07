class Game:
 
    def __init__(self, matchID, localTeam, visitTeam, date, time, location, result, pitcherLocal, pitcherVisit, lineupBatLocal, lineupBatVisit, runs, hits, errors, prediction):
        self.gameID = gameID
        self.localTeam = localTeam
        self.visitTeam = visitTeam
        self.date = date
        self.time = time
        self.location = location
        self.result = result
        self.pitcherLocal = pitcherLocal
        self.pitcherVisit = pitcherVisit
        self.lineupBatLocal = lineupBatLocal
        self.lineupBatVisit = lineupBatVisit
        self.runs = runs
        self.hits = hits
        self.errors = errors
        self.prediction = prediction
    
    def getID(self):
        return gameID

    def getLocal(self):
        return localTeam
    def getVisit(self):
        return visitTeam
    def getDate(self):
        return date
    def getTime(self):
        return time
    def getLocation(self):
        return location
    def getPitcherLocal(self):
        return pitcherLocal
    def getPitcherVisit(self):
        return pitcherVisit
    def getLineupBatLocal(self):
        return lineupBatLocal
    def getLineupBatVisit(self):
        return lineupBatVisit
    def getRuns(self):
        return runs
    def getHits(self):
        return hits
    def getErrors(self):
        return errors
    def getPrediction(self):
        return prediction