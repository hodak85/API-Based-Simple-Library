import requests
import pytest


def post_request(url, json_string):
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json_string, headers=headers)
    return r


def get_request(url):
    r = requests.get(url)
    return r


test_data_search_book = [
        ("admin", "admin", "", "", ""),
        ("admin", "test", "", "a1", ""),
        ("test", "admin", "1", "a1", "b1"),
        ("admin", "admin", "", "a1", "b1"),
        ("admin", "admin", "", "a1", "b2"),
        ("", "admin", "", "a1", "b1")
        ]

@pytest.mark.parametrize("usr,pswd,item_id,title,author", test_data_search_book)
def test_search_books(usr, pswd, item_id, title, author):
    my_args = []
    if usr != "":
        my_args.append("usr=%s" %(usr))
    if pswd != "":
        my_args.append("pswd=%s" %(pswd))
    if item_id != "":
        my_args.append("item_id=%s" %(item_id))
    if title != "":
        my_args.append("title=%s" %(title))
    if author != "":
        my_args.append("author=%s" %(author))
    parameters = '&'.join(my_args)

    url = "http://127.0.0.1/search/books/?%s" %(parameters)
    print(url)
    response = get_request(url)
    assert (response.status_code == 200 or response.status_code == 422)

test_data_search_user = [
        ("admin", "admin", "", ""),
        ("admin", "test", "", ""),
        ("test", "admin", "1", "test1"),
        ]

@pytest.mark.parametrize("usr,pswd,user_id,user", test_data_search_user)
def test_search_users(usr, pswd, user_id, user):
    my_args = []
    if usr != "":
        my_args.append("usr=%s" %(usr))
    if pswd != "":
        my_args.append("pswd=%s" %(pswd))
    if user_id != "":
        my_args.append("user_id=%s" %(user_id))
    if user != "":
        my_args.append("user=%s" %(user))
    parameters = '&'.join(my_args)  

    url = "http://127.0.0.1/search/users/?%s" %(parameters)
    print(url)
    response = get_request(url)
    assert (response.status_code == 200 or response.status_code == 422)



test_data_add_book = [
        ("admin", "admin", "", "", ""),
        ("admin", "test", "", "a1", ""),
        ("test", "admin", "a1", "test1", ""),
        ("admin", "admin", "a1", "b2", ""),
        ("admin", "admin", "a1", "b2", "2021-02-01"),
        ("admin", "admin", "", "b3", "")
        ]
@pytest.mark.parametrize("usr,pswd,title,author,pub_date", test_data_add_book)
def test_add_book(usr,pswd,title,author,pub_date):
    json_string = {"item": {}, "user": {}}

    if usr != "":
        json_string["user"]["user"] = usr
    if pswd != "":
        json_string["user"]["password"] = pswd
    if title != "":
        json_string["item"]["title"] = title
    if author != "":
        json_string["item"]["author"] = author
    if pub_date != "":
        json_string["item"]["pub_date"] = pub_date

    url = "http://127.0.0.1/book/add/"
    response = post_request(url, json_string)
    
    assert (response.status_code == 200 or response.status_code == 422)

test_data_update_book = [
        ("admin", "admin", "1"),
        ("admin", "admin", ""),
        ("test", "admin", "a1"),
        ("test", "admin", "1")
        ]
@pytest.mark.parametrize("usr,pswd,item_id", test_data_update_book)
def test_update_book(usr,pswd,item_id):
    json_string = {"user": "", "password": ""}
    if usr != "":
        json_string["user"] = usr
    if pswd != "":
        json_string["password"] = pswd

    if item_id != "":
        param = item_id
    else:
        param = 0

    url = "http://127.0.0.1/book/lent/%s" %(param)
    response = post_request(url, json_string)
    print(response)
    assert (response.status_code == 200 or response.status_code == 422)
