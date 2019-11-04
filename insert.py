import pymysql


#player hitting
def playerHitting(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. KHendricksCHC
    id = mylist[0].replace(",", "").split()
    id = id[1] + id[0] + mylist[1]

    insertPlayer = "INSERT INTO player VALUES (\"%s\", \"%s\", \"%s\", \"%s\");" % (
        id,
        mylist[0],
        mylist[1],
        mylist[2],
    )

    insertPlayerStats = "INSERT INTO playerstats VALUES (\"%s\", \"HITTING\", %s, %s, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, NULL, NULL);" % (
        id,
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        mylist[9],
    )

    print(insertPlayer)
    print(insertPlayerStats)

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert data")


#player pitching
def playerPitching(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS
    id = mylist[0].replace(",", "").split()
    id = id[1] + id[0] + mylist[1]

    insertPlayer = "INSERT INTO player VALUES (\"%s\", \"%s\", \"%s\", \"P\");" % (
        id,
        mylist[0],
        mylist[1],
    )

    insertPlayerStats = "INSERT INTO playerstats VALUES (\"%s\", \"PITCHING\", %s, %s, %s, NULL, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL);" % (
        id,
        mylist[2],
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        mylist[9],
    )

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert data")


#player fielding
def playerFielding(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    #id = inicial + apellido + equipo
    #ej. JBeeksBOS
    id = mylist[0].replace(",", "").split()
    id = id[1] + id[0] + mylist[1]

    insertPlayer = "INSERT INTO player VALUES (\"%s\", \"%s\", \"%s\", \"%s\");" % (
        id,
        mylist[0],
        mylist[1],
        mylist[2],
    )

    insertPlayerStats = "INSERT INTO playerstats VALUES (\"%s\", \"FIELDING\", %s, %s, NULL, NULL, NULL, NULL, NULL, NULL, NULL, %s, %s, %s, %s, %s);" % (
        id,
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
        mylist[9],
    )

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert data")