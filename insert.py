import pymysql


#player hitting
def playerHitting(db, *args):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    mylist = list(args)

    insertPlayer = "INSERT INTO jugador VALUES (NULL, \"%s\", \"%s\", \"%s\");" % (
        mylist[0],
        mylist[1],
        mylist[2],
    )

    insertPlayerStats = "INSERT INTO jugadorstats VALUES (NULL, \"HITTING\", %s, %s, %s, %s, %s, %s, NULL, NULL, NULL, NULL, NULL, NULL, NULL);" % (
        mylist[3],
        mylist[4],
        mylist[5],
        mylist[6],
        mylist[7],
        mylist[8],
    )

    #print(insertPlayer)
    #print(insertPlayerStats)

    try:
        cursor.execute(insertPlayer)
        db.commit()
        cursor.execute(insertPlayerStats)
        db.commit()
    except:
        print("Error: Unable to insert data")
