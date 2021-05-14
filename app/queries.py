import MySQLdb

mysqldb = MySQLdb.connect(host='db', port=3306, user='root', password='h0Da', db='mylib')


#Select Query
def select_query(query):
    cur = mysqldb.cursor()
    cur.execute(query)
    myresult = cur.fetchall()
    return myresult

#Insert OR Update Query
def insupd_query(query):
    cur = mysqldb.cursor()
    cur.execute(query)
    myresult = mysqldb.commit()
    return myresult

