import csv
import time
import os

def clear():
    os.system("clean")
f = open("accnos.txt","r")
newaccno = f.read()
f.close()
f = open("accnos.txt","w")
n = int(newaccno) + 1
n = str(n)
f.write(n)
f.close()

#format = [Name, Aadhar No, Amount, Pin, Acc No]
data = []
name = input("Enter your name : ")
data.append(name)
time.sleep(0.8)
clear()

f = open("aadhaar.csv","r")
ff = csv.reader(f)
aadhars = []

for i in ff:
    aadhars.append(i)

while True:
    adh = input("Enter your aadhar no :")
    if adh in aadhars:
        print("Aadhar no already in use.")
        print()
        input("Press Enter to continue")
        clear()
        continue
    else:
        data.append(adh)
        time.sleep(0.8)
        clear()
        break

while True:
    amt = int(input("Enter amount to be added : "))
    if amt < 2000:
        print("Minimum Balance should be 2000")
        print();input("Press Enter to continue"); clear()
