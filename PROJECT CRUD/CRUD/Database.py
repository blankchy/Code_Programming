from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "title":255*" ",
    "author":255*" ",
    "year":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database Available, init done!")
    except:
        print("Database Can't Acces, Please Create New Databas")
        Operation.create_first_data()
        
            