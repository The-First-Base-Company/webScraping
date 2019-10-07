class Player:
 
    def __init__(self, playerID, firstN, lastN, age, positi, team, hit, pitch, field, rank):
        self.playerID = playerID
        self.firstN = firstN
        self.lastN = lastN
        self.age = age
        self.position = position
        self.team = team
        self.hit = hit
        self.pitch = pitch
        self.field = field
        self.rank = rank

    def getID(self):
        return playerID

    def getName(self):
        return '{} {}'.format(self.firstN, self.lastN)
    def getAge(self):
        return age
    def getPosition(self):
        return position
    def getTeam(self):
        return team
    def getHit(self):
        return hit
    def getPitch(self):
        return pitch
    def getField(self):
        return field
    def getRank(self):
        return rank
    
"""
    # def getTeam(self):
    #    return self.team

    def getStats(self):
        return 'Hit: {}, Pitching: {}, Fielding: {}'.format(self.hit, self.pitch, self.field)


player1 = Player('Andres', 'Cebolla', 'Red Sox', 3.2, 1.3, 2)
# player1.hit = 1.3
# print(player1.hit)

# print(Player.getName(player1))
print(player1.getName())
print(player1.team)
"""
