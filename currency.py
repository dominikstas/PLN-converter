import sqlite3

db = sqlite3.connect("currency.db")
cursor = db.cursor()

#make database of currency, id of currency and site with the real time price
money = 0
currency = str
valid = 0
result = float
result1 = float

def main():
    while money == 0:
        input_value()
    while valid == 0:
        input_currency()
    convert_buy(money, valid)
    convert_sell(money, valid)
    print(f'buy = {result}\nsell = {result1}')
    
    
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
        global valid
        global currency
        currency =  str(input("What's currency? "))
        check_currency(currency)
        if valid == 0:
            raise ValueError
    except ValueError:
        print("Please enter valid name. ")

def check_currency(currency):
    global valid 
    sql_select_query = """select * from currency where name like ?"""
    cursor.execute(sql_select_query, (currency,))
    id = cursor.fetchall()
    for row in id:
           valid += row[0]

         

     
def show():
     cursor.execute('''
                    select *
                    from currency
                    ''')
     
     rows = cursor.fetchall()
     for r in rows:
          print(r[1],r[2],r[3])


def convert_sell(money, valid):
    global result1
    sql_select_query = """select sell from currency where id=?"""
    cursor.execute(sql_select_query, (valid,))
    _ = cursor.fetchall()
    for row in _:
         result1 = money*row[0]
         return result1


def convert_buy(money,valid):
    global result
    sql_select_query = """select buy from currency where id=?"""
    cursor.execute(sql_select_query, (valid,))
    _ = cursor.fetchall()
    for row in _:
         result = money*row[0]
         return result

main()





