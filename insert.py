import pymysql


#player hitting
def playerHitting(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. KHendricksCHC
    id = mylist[1].replace(" ", "")
    id = id + mylist[2]

    print(
        id,
        mylist[0],
        mylist[1],
        mylist[2],
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        mylist[9],
        mylist[10],
        mylist[11],
        mylist[12],
        mylist[13],
    )
    insertPlayer = "INSERT INTO player VALUES (\"%s\", \"%s\", \"%s\", \"%s\", %s, %s, \"%s\", \"%s\", %s, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %s, NULL, NULL);" % (
        id,
        mylist[0],
        mylist[1],
        mylist[2],
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        mylist[9],
        mylist[10],
        mylist[11],
        mylist[12],
        mylist[13],
    )

    print(insertPlayer)

    insertPlayerStats = "INSERT INTO playerstats VALUES (\"%s\", %s, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, NULL, NULL);" % (
        id,
        mylist[14],
        mylist[15],
        mylist[16],
        mylist[17],
        mylist[18],
        mylist[19],
    )

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert hitting data")


#player pitching
def playerPitching(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS
    id = mylist[1].replace(" ", "").split()
    id = id + mylist[2]

    insertPlayer = "INSERT INTO player VALUES (\"%s\", \"%s\", \"%s\", \"%s\", %s, %s, \"%s\", \"%s\", %s, \"%s\", \"%s\", \"%s\", \"%s\", NULL, NULL, %s, NULL);" % (
        id,
        mylist[0],  #foto
        mylist[1],  #nombre
        mylist[2],  #numero
        mylist[3],  #altura
        mylist[4],  #edad
        mylist[5],  #apodo
        mylist[6],  #nacimiento DATE
        mylist[7],  #draft year
        mylist[8],  #draft team
        mylist[9],  #draft round
        mylist[10],  #debut DATE
        mylist[11],  #equipo
        mylist[12],  #rank
    )

    insertPlayerStats = "INSERT INTO playerstats VALUES (\"%s\", %s, %s, NULL, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL);" % (
        id,
        mylist[13],
        mylist[14],
        mylist[15],
        mylist[16],
        mylist[17],
        mylist[18],
        mylist[19],
    )

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert pitching data")


#player fielding
def playerFielding(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS
    id = mylist[0].replace(" ", "")
    id = id + mylist[1]

    insertPlayer = "UPDATE player SET POSICION = \"%s\", RANKF = %s WHERE ID = \"%s\";" % (
        mylist[2],
        mylist[3],
        id,
    )

    insertPlayerStats = "UPDATE playerstats SET OPORTUNIDADES = %s, PUTOUT = %s, ASISTENCIAS = %s, ERRORES = %s, AVGERRORES = %s WHERE ID = \"%s\";" % (
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        id,
    )
    #print(insertPlayer)
    #print(insertPlayerStats)
    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert fielding data")


def teamHitting(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    teamNames = [
        "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles",
        "Boston Red Sox", "Chicago Cubs", "Chicago White Sox",
        "Cincinnati Reds", "Cleveland Indians", "Colorado Rockies",
        "Detroit Tigers", "Houston Astros", "Kansas City Royals",
        "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins",
        "Milwaukee Brewers", "Minnesota Twins", "New York Mets",
        "New York Yankees", "Oakland Athletics", "Philadelphia Phillies",
        "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants",
        "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays",
        "Texas Rangers", "Toronto Blue Jays", "Washington Nationals"
    ]

    teamAbbrev = [
        "ARI", "ATL", "BAL", "BOS", "CHC", "CWS", "CIN", "CLE", "COL", "DET",
        "HOU", "KC", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK",
        "PHI", "PIT", "SD", "SF", "SEA", "STL", "TB", "TEX", "TOR", "WSH"
    ]
    i = 0
    for team in teamNames:
        if (teamNames[i] == mylist[0]):
            abbrev = teamAbbrev[i]
        i += 1

    insertTeam = "INSERT INTO team VALUES (\"%s\", \"%s\", \"%s\", %s, NULL, NULL);" % (
        mylist[0],
        abbrev,
        mylist[1],
        mylist[9],
    )

    insertTeamStats = "INSERT INTO teamstats VALUES (\"%s\", %s, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);" % (
        mylist[0],
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
    )

    try:
        #print(insertTeam)
        #print(insertTeamStats)
        cursor.execute(insertTeam)
        db.commit()
        cursor.execute(insertTeamStats)
        db.commit()
    except:
        print("Error: Unable to insert data")


#
def teamPitching(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS

    insertTeam = "UPDATE team SET ERANKP = %s WHERE ENOMBRE = \"%s\" ;" % (
        mylist[7],
        mylist[0],
    )

    insertTeamStats = "UPDATE teamstats SET ERUNSALLOWED = %s, EHITSALLOWED = %s, EHRALLOWED = %s, EAVGHITSA = %s, EWINS = %s , ELOSSES = %s WHERE ENOMBRE = \"%s\" ;" % (
        mylist[1],
        mylist[2],
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[0],
    )

    try:
        #   print(insertTeam)
        #print(insertTeamStats)
        cursor.execute(insertTeam)
        db.commit()
        cursor.execute(insertTeamStats)
        db.commit()
    except:
        print("Error: Unable to insert data")


#
def teamFielding(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS

    insertTeam = "UPDATE team SET ERANKF = %s WHERE ENOMBRE = \"%s\" ;" % (
        mylist[6],
        mylist[0],
    )

    insertTeamStats = "UPDATE teamstats SET EOPORTUNIDADES = %s, EPUTOUT = %s, EASISTENCIAS = %s, EERRORES = %s, EAVGERRORES = %s WHERE ENOMBRE = \"%s\" ;" % (
        mylist[1], mylist[2], mylist[3], mylist[4], mylist[5], mylist[0])

    try:
        cursor.execute(insertTeam)
        db.commit()
        #print(insertTeamStats)
        cursor.execute(insertTeamStats)
        db.commit()
    except:
        print("Error: Unable to insert data")

def teamInfo(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS

    insertTeam = "UPDATE team SET LOGO = \"%s\", WEB = \"%s\", ESTADIO = \"%s\" WHERE ENOMBRE = \"%s\" ;" % (
        mylist[0],
        mylist[1],
        mylist[2],
        mylist[3],
    )

    try:
        cursor.execute(insertTeam)
        db.commit()
    except:
        print("Error: Unable to insert data")