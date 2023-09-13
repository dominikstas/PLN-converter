import sqlite3

db = sqlite3.connect("currency.db")
cursor = db.cursor()

#make database of currency, id of currency and site with the real time price
money = 0
currency = str

def main():
    while money == 0:
        input_value()
    input_currency()
    
#take an input from user what


#input how many
def input_value():
        try:
            global money 
            money = float(input("How much? (Deafult currency is PLN). If you want check current prices, enter '0' "))
            if money == 0:
                 show()
                 input_value()
            return(money)
        except ValueError:
            print("You must enter the number.")
    
  

#input to what
def input_currency():
    try:
        global currency
        currency =  str(input("What's currency? "))
        check_currency(currency)
        if check_currency == "valid":
             return(currency)
    except ValueError:
        print("Please enter valid name. ")

def check_currency(currency):
     currency
     
def show():
     cursor.execute('''
                    select *
                    from currency
                    ''')
     
     rows = cursor.fetchall()
     for r in rows:
          print(r[1],r[2],r[3])

main()




#convert and print the result
