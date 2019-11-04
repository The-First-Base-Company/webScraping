import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "", "tarea3")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM dept"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print(results)
    for row in results:
        deptno = row[0]
        dname = row[1]
        loc = row[2]
        # Now print fetched result
        print("deptno = %d,dname = %s,loc = %s" % (deptno, dname, loc))
except:
    print("Error: unable to fetch data")

# disconnect from server
db.close()