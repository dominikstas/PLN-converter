#make database of currency, id of currency and site with the real time price
money = 0
currency = str

def main():
    while money == 0:
        input_value()
    input_currency()
    check_currency(currency)
#take an input from user what


#input how many
def input_value():
        try:
            global money 
            money = float(input("How much? "))
            return(money)
        except ValueError:
            print("You must enter the number.")
    
  

#input to what
def input_currency():
    try:
        global currency
        currency =  str(input("What's currency? "))
        return(currency)
    except ValueError:
        print("Please enter valid name. ")

def check_currency(currency):
     currency


main()




#convert and print the result
