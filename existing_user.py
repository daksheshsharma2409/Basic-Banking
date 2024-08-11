import csv
import os
import time

#format = [Name, Aadhar No, Amount, Pin, Acc No]

def clean():
    os.system("clear")

f1 = open("data.csv","r")
f = csv.reader(f1)
ids = []
names = []
balance = []
pins = []
adh = []
for i in f:
    ids.append(i[4])
    names.append(i[0])
    balance.append(i[2])
    pins.append(i[3])
    adh.append(i[1])
def updating():
    datalist = []
    for i in range(0,len(ids)):
        datalist.append(names[i])
        datalist.append(adh[i])
        datalist.append(balance[i])
        datalist.append(pins[i])
        datalist.append(ids[i])
    print(datalist)
    fc = open("data.csv","w",newline="")
    f = csv.writer(fc,delimiter=",")
    n = 0
    for j in range(0,len(names)):
        nl = []
        try:
            for k in range(0,len(name)+1):
                nl.append(datalist[n])
                n = n+1
            f.writerow(nl)
        except:
            print()
updating()
while True:
    acc_no_enter = input("Enter your Account No : ")
    print()
    if acc_no_enter not in ids:
        print("Account not found please enter a valid no. ")
        print()
        input("Press Enter to try again")
        clean()
        continue
    else :
        user_index = ids.index(acc_no_enter)
        print()
        break
while True:
    pin_enter = input("Enter pin : ")
    correct_pin = pins[user_index]
    print()
    if pin_enter != correct_pin:
        print("Wrong Pin")
        print("Press Enter to Try Again")
        input()
        print()
        clean()
        continue
    if pin_enter == correct_pin:
        print()
        time.sleep(0.5)
        clean()
        break
while True:
    print(f"Welcome {names[user_index]}")
    print(); print()
    print("What feature would you like to use : ")
    print()
    print("'1' : Check current balance.")
    print("'2' : Deposit money")
    print("'3' : Withdraw money")
    print("'4' : Transfer money to other account")
    print("'5' : Log Out")
    print()
    opt = int(input("Choose Option from above (1/2/3/4/5) : "))

    if opt == 1:
        print(f"Current Balance >> Rs {balance[user_index]}")
        input("Press Enter to continue")
        print()
        clean()
        continue
    if opt == 2:
        while True:
            depoamt = int(input("Enter money to be deposited : "))
            if depoamt < 1000:
                print("Minimum amount to be deposited is Rs 1000")
                print()
                input("Press Enter to continue")
                clean()
                continue
            else:
                balance[user_index] = int(balance[user_index]) + depoamt
                print(f"New balance >>> {balance[user_index]}")
                print()
                input("Press Enter to continue")
                break
    if opt == 3:
        pass
    if opt == 4:
        pass
    if opt == 5:
        time.sleep(0.7)
        clean()
        break




