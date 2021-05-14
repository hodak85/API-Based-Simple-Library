from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from app import schemas
import MySQLdb



mysqldb = MySQLdb.connect(host='db', port=3306, user='root', password='h0Da', db='mylib')

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "There are two Endpoints provided addBook and books!"}

@app.post("/addBook/")
async def add_item(item: schemas.Book):

    if item.pub_date:
        values =  "('%s', '%s', '%s')" %(item.title, item.author, item.pub_date) #2021-05-13
    else:
        values = "('%s', '%s', NULL)" %(item.title, item.author)
    
    cur = mysqldb.cursor()
    mysqlq = "insert into book (title, author, pub_date) values %s " %(values)
    try:
        cur.execute(mysqlq)
        mysqldb.commit()
    except:
        return {"message": "invalid arguments are used!"}

    if cur.rowcount > 0:
        res = {"message": "successfully inserted!"}
    else:
        res = {"message": "operation failed!"}

    return res

@app.get("/books/{item_id}")
def get_book(item_id: int):
    cur = mysqldb.cursor()
    cur.execute("SELECT * FROM book where id = %d" %(item_id))
    myresult = cur.fetchall()

    if cur.rowcount > 0:
        res = {"title": myresult[0][1], "author": myresult[0][2], "publish_date": myresult[0][3]}
    else:
        res = {"message": "No Record is Found!"}
    return res
