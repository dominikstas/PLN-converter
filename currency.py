#make database of currency, id of currency and site with the real time price
def main():
    money = 0
    input_value()
#take an input from user what


#input how many
def input_value():
    while money == 0:
        try:
            money = float(input("How much? "))
        except ValueError:
            print("You must enter the number.")
  

#input to what




main()




#convert and print the result
