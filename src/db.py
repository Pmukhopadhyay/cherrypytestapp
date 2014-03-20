import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost",user="vertexbusiness",passwd="password",db="vertexbusiness")
cur = db.cursor()
cur.execute("SELECT * FROM Device")
col_names = [i[0] for i in cur.description]
for row in cur.fetchall() :
    i = 0
    for col in col_names :
        print row[i]
        i=i+1
    print '\n'
