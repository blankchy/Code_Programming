from . import Operation

def delete_console():
    read_console()
    while(True):
        print("\n"+"-"*50)
        print("(Input number-book Delete)")
        print("-"*50+"\n")
        number_book = int(input("Input Book Number: "))
        data_book = Operation.read(index=number_book)
    
        if data_book:
            data_break = data_book.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            author = data_break[2]
            title = data_break[3]
            year = data_break[4][:-1]
                    
            # Data Delete
            print("="*100)
            print("Option: Please Input Data (Delete)")
            print(f"1. Author\t: {author:.40}")
            print(f"2. Title\t: {title:.40}")
            print(f"3. Years\t: {year:4}")
            is_done = input("Data Delete Done? (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operation.delete(number_book)
                break
        else:
            print("-"*50)
            print("Number book-valid, please insert book again!")
            print("-"*50+"\n")

    print("Data Has Been deleted !")

def update_console():
    read_console()
    while(True):
        print("-"*50)
        print("(Input number-book Update)")
        print("-"*50+"\n")
        number_book = int(input("Input Book Number: "))
        data_book = Operation.read(index=number_book)
    
        if data_book:
            break
        else:
            print("\n"+"-"*50)
            print("Number book-valid, please insert book again!")
            print("-"*50+"\n")

    data_break = data_book.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    author = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]


    while(True):
        # Data Update
        print("\n"+"="*100)
        print("Option: Please Input Data (Update)")
        print(f"1. Author\t: {author:.40}")
        print(f"2. Title\t: {title:.40}")
        print(f"3. Years\t: {year:4}")

        # Option Data changed
        user_option = input("Section Option Input [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": author = input("Author\t: ")
            case "2": title = input("Title\t: ")
            case "3":
                while(True):
                    try:
                        year = int(input("Years\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("Input haas been 4 digit (year)!")    
                    except:
                        print("Input years must be number or 4 digit (yyyy)")
            case _: print("Data hasn't been changed!")
        
        print("New Data Changes (Update)!")
        print(f"1. Author\t: {author:.40}")
        print(f"2. Title\t: {title:.40}")
        print(f"3. Years\t: {year:4}")
        is_done = input("Data Update Done? (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operation.update(number_book,pk,data_add,author,title,year)


def create_console():
    print("\n\n"+"="*100)
    print("Please Add New_Database Library\n")
    author = input("Author\t: ")
    title = input("Title\t: ")
    while(True):
        try:
            year = int(input("Years\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("Input haas been 4 digit (year)!")    
        except:
            print("Input years must be number or 4 digit (yyyy)")

    Operation.create(year,title,author)
    print("\nProgram Has Been Created!")
    read_console()

def read_console():
    data_file = Operation.read()
    
    index = "No"
    title = "Title"
    author = "Author"
    year = "Years"

    # Header
    print("\n"+"="*100)
    print(f"{index:<4} | {author:40} | {title:40} | {year:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        author = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:<4} | {author:.40} | {title:.40} | {year:4}",end="")

    # Footer
    print("="*100+"\n")