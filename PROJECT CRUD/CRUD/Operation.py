from time import time
from . import Database
from .Utility import random_string
import time
import os

def delete(number_book):
    try:
        with(open(Database.DB_NAME,'r')) as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == number_book - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database Error!")
    
    # Delete the existing file if it exists
    if os.path.exists(Database.DB_NAME):
        os.remove(Database.DB_NAME)

    os.rename("data_temp.txt",Database.DB_NAME)

def update(number_book,pk,data_add,author,title,year):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'

    data_length = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file :
            file.seek(data_length*(number_book-1))
            file.write(data_str)
    except:
        print("Data in-Database (Update) Error!")



def create(year,title,author):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data Can't Access, Please Correct Data in Database (data.txtt)")

def create_first_data():
    author = input("Author: ")
    title = input("Title: ")
    while(True):
        try:
            year = int(input("year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("Input haas been 4 digit (year)!")    
        except:
            print("Input years must be number or 4 digit (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["author"]},{data["title"]},{data["year"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data failed input database!")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            result_book = len(content)
            if "index" in kwargs:
                index_book = kwargs["index"]-1
                if index_book < 0 or index_book > result_book:
                    return False
                else:
                    return content[index_book]
            else:
                return content
    except:
        print("Reading database error")
        return False
    
