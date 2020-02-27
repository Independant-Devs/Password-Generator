import random
import time
def welcome():
    print("PasswordGenerator Pro, v2.0 ")
    print()
    print("</*\> Welcome on Password Generator Ultimate </*\>")
    print()
    print()
    print("Made by Wafelack")
    print()
    print()
def space():
    print()
    print()
    print()
    print()
    print()
    print()
def choicer():
    print()
    choice = input("Do you want to retry [Y/N] ? > ")
    if(choice == "Y"):
        space()
        main()
    if(choice == "N"):
        print("Thanks for using Password Generator")
        time.sleep(2)
        exit()
def main():
    firstCar = 0
    lastCar = 63
    print("Choose your password's length (from 4 to 16)")
    print()
    length = input("[password@length]$ ")
    print()
    print()
    cars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z","_","-","."]
    if(length == '4'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '5'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '6'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '7'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '8'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '9'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '10'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '11'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '12'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '13'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '14'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '15'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer()
    if(length == '16'):
        print(cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)] + cars[random.randint(firstCar,lastCar)])
        choicer() 
    else:
        print("Syntax Error : value not supported")
        choicer()
welcome()
main()