print ("WEllCOME STORE APPLICATION ")

import qrcode

PRODUCTS = []

def read_from_database () :
    f = open ("E:\Python\jalase 7\Assignment-7\database.txt" , "r")

    for line in f :
        x = line.split("\n")
        y = x[0]
        result = y.split (",")
        product = { "code" : result[0] , "name" : result[1] , "price" : result[2] , "count" : result[3] }
        PRODUCTS.append ( product )

    f.close ()


def show_menue () :
    print (" print 1 to Add ")
    print (" print 2 to Edit ")
    print (" print 3 to Remove ")
    print (" print 4 to Search ")
    print (" print 5 to Show ")
    print (" print 6 to Buy ")
    print (" print 7 to make a QR code for a product")
    print (" print 8 to Exit ")


def add () :
    code = input (" Please enter product's code : ")
    name = input (" Please enter product's name : ")
    price = input (" Please enter product's price : ")
    number = input (" Please enter product's count : ")
    new_product = { "code" : code , "name" : name , "price" : price , "count" : number }
    PRODUCTS.append ( new_product )


def edit () :
    user_choice = input (" Please enter prodect's code : ")
    for product in PRODUCTS :
        if product["code"] == user_choice :
            print (" The product found ")
            print (" What do you want to change about this product ? ( name , price or count ) ")
            change = input (" Please enter your choice : ")
            if change == "name":
                new = input (" Please enter new name : ")
                product["name"] = new
                print (" information updated successfully ")
                break

            elif change == "price" :
                new = input (" Please enter new price : ")
                product["price"] = new
                print (" information updated successfully ")
                break

            elif change == "count" :
                new = input (" Please enter new count : ")
                product["count"] = new
                print (" information updated successfully ")
                break

            else :
                print (" Wrong input ")
                break
    
    else :
        print (" Wrong code ")
        print (" The product hasn't been found ")


def remove () :
    user_choice = input (" Please enter product's code : ")
    for product in PRODUCTS :
        if product["code"] == user_choice :
            PRODUCTS.remove ( product )
            print (" Product removed successfully ")
            break
    
    else :
        print (" Wrong code ")
        print (" The product hasn't been found ")


def search () :
    user_check = input (" Please enter the name or the code of the product you are looking for : ")
    for product in PRODUCTS :
        if product["code"] == user_check or product["name"] == user_check :
            print (" Found ")
            print ( product["code"], "\t\t", product["name"], "\t\t", product["price"] )
    
    else :
        print (" Not found ")


def show_list () :
    print ("code\t\tname\t\tprice")
    for product in PRODUCTS :
        print (product["code"], "\t\t", product["name"], "\t\t", product["price"])


def buy () :
    print (" print 'Done' when you finish shopping ")
    Factor = []
    final_cost = 0
    
    while True :    
        user_choice = input(" Please enter the product's code : ")
        
        if user_choice == "done" :
            print ("name\t\tcount\t\tfee\t\tcost")
            for product in Factor :
                print ( product["name"] , "\t\t" , product["tedad"] , "\t\t" , product["price"] , "\t\t" , product["cost"])
                final_cost = final_cost + int( product["cost"] )
            
            print (" final cost : ", final_cost)
            break

        else :
            for product in PRODUCTS :
                if product["code"] == user_choice :
                    print (" We have this product ")
                    number = int ( input (" How many do you want : "))
                    count = int ( product["count"] )
                    if number <= count :
                        print ("OK! What else ?")
                        store = count - number
                        product["count"] = str ( store )                                    
                        price = int ( product["price"] )
                        cost = number * price
                        new_purchase = {"name" : product["name"] , "tedad" : number , "price" : product["price"] , "cost" : cost }
                        Factor.append ( new_purchase )

                    else :
                        print (" We don't have this many ")

                    break
            
            else :
                print (" There is not any product with this code number ")

def qrcode_maker () :
    user_choice = input (" Please enter product's code : ")
    for product in PRODUCTS :
        if product["code"] == user_choice :
            print (" product found ")
            x = qrcode.make ( product )
            x.save ("E:\Python\jalase 7\Assignment-7\product QR code.png ")
            break
    
    else :
        print (" Wrong code ")
        print (" The product hasn's been found")

def save_to_database () :
    f = open ("E:\Python\jalase 7\Assignment-7\database.txt" , "w")
    for product in PRODUCTS :
        txt = product["code"] + "," + product["name"] + "," + product["price"] + "," + product["count"] + "\n"
        f.write ( txt )

    f.close


print (" Wellcome to My store ")
print (" Loading... ")
read_from_database ()
print (" data loaded ")

while True :
    show_menue ()
    choice = int ( input (" Please enter your choice from menue : "))

    if choice == 1 :
        add ()
    
    elif choice == 2 :
        edit ()
    
    elif choice == 3 :
        remove ()

    elif choice == 4 :
        search ()

    elif choice == 5 :
        show_list ()

    elif choice == 6 :
        buy ()
    
    elif choice == 7 :
        qrcode_maker ()

    elif choice == 8 :
        save_to_database ()
        exit (0)

    else :
        print (" What you entered is not defined ")
        print (" Please try again ")