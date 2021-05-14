from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from app import schemas, queries
import hashlib


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "There are two Endpoints provided addBook and books!"}

#Add new book
@app.post("/book/add/")
async def add_item(item: schemas.Book, user: schemas.User):
    #user authentication
    if not validate(user.user, user.password):
        return {"message":"Check your credentials!"}

    #prepare for insertion
    if item.pub_date:
        values =  "('%s', '%s', '%s')" %(item.title, item.author, item.pub_date) #2021-05-13
    else:
        values = "('%s', '%s', NULL)" %(item.title, item.author)
    
    mysqlq = "insert into book (title, author, pub_date) values %s " %(values)
    try:
        myresult = queries.insupd_query(mysqlq)
        return {"message": "successfully inserted!"}
    except:
        return {"message": "invalid arguments are used!"}



#Add update book existance
@app.post("/book/lent/{item_id}")
async def lent_item(item_id: int , user: schemas.User):
    #user authentication
    if not validate(user.user, user.password):
        return {"message":"Check your credentials!"}
    
    
    mysqlq = "update book set existance = 0 where id = %d" %(item_id)
    try:
        myresult = queries.insupd_query(mysqlq)
        return {"message": "successfully updated!"}
    except:
        return {"message": "invalid arguments are used!"}



#search in books 
@app.get("/search/books/")
def get_book(usr: str, pswd: str, item_id: Optional[int] = None, title: Optional[str] = None, author: Optional[str] = None):

    #user authentication
    if not validate(usr, pswd):
        return {"message":"Check your credentials!"}

    my_args = []
    #select query
    if item_id != None:
        if type(item_id) != int :
            return {"message": "invalid arguments are used!"}
        my_args.append("id = %d" %(item_id))
    if title != None:
        my_args.append("title = '%s'" %(title))
    if author != None:
        my_args.append("author = '%s'" %(author))
    
    if len(my_args) == 0:
        wh = "1=1"
    else:
        wh = " and ".join(my_args) 

    qry = "SELECT * FROM book where %s" %(wh)
    myresult = queries.select_query(qry)

    #handle the reponse from db
    if len(myresult) > 0:
        return {"id":myresult[0][0] ,"title": myresult[0][1], "author": myresult[0][2], "publish_date": myresult[0][4], "existance": myresult[0][3]}
    else:
        return {"message": "No Record is Found!"}


#search in users 
@app.get("/search/users/")
def get_user(usr: str, pswd: str, user_id: Optional[int] = None, user: Optional[str] = None):
    #user authentication
    if not validate(usr, pswd):
        return {"message":"Check your credentials!"}

    my_args = []
    #select query
    if user_id != None:
        if type(item_id) != int :
            return {"message": "invalid arguments are used!"}
        my_args.append("id = %d" %(user_id))
    if user != None:
        my_args.append("user = '%s'" %(user))

    if len(my_args) == 0:
        wh = "1=1"
    else:
        wh = " and ".join(my_args)

    qry = "SELECT * FROM user where %s" %(wh)
    myresult = queries.select_query(qry)

    #handle the reponse from db
    if len(myresult) > 0:
        return {"id":myresult[0][0] ,"user": myresult[0][1]}
    else:
        return {"message": "No Record is Found!"}


#Authentincation
def validate(user, password):
    pswd = hashlib.md5(str(password).encode('utf-8')).hexdigest()
    qry = "SELECT * FROM user where user='%s' and password='%s'" %(user, pswd)
    myresult = queries.select_query(qry)
    if len(myresult) > 0:
        return True
    else:
        return False


