from subprocess import call
import os
import time 
def clean():
    os.system("clear")
def callfxn(f):
    call(["python",f])
while True:
    print("If you are existing user select option '1' ")
    print("If you are new user select option '2' ")
    print("Select option '3' to exit")

    while True:
        option = int(input("Select the option from above : "))

        if option not in [1,2,3]:
            print("Please select from the options given only.")
            print()
            continue
        else:
            print()
            time.sleep(1.2)
            clean()
            break

    if option == 1:
        callfxn("existing_user.py")


    if option == 2:
        pass

    if option == 3 :
        print("Goodbye!")
        time.sleep(0.7)
        clean()
        break

