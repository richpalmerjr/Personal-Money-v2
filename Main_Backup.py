import os
import csv

#set the working directory
os.chdir(r"C:\Users\richp\OneDrive\Desktop\Python Projects\Money 2.0")

textFile = "ReadThisFile.txt"

textFile = open(textFile,"r")
csvFile = open("Money.csv","w",newline="")
money_writer = csv.writer(csvFile, delimiter=",")

total=float(0)

###########################
for x in textFile:
    line = x.split("\t")
    date = line[0].replace("\n","")
    type = line[1].replace("\n","")
    amount = float(line[2].replace("$","").replace(",","").replace("\n",""))
    balance = float(line[3].replace("$","").replace(",","").replace("\n",""))
    total = total + amount
    #print(date,type,amount,balance)

    if "-" in type:
        withdrawOrDeposit = type.split(" - ")[0]
        what = type.split(" - ")[1]
        print(type.split(" - ")[1])
    else:
        withdrawOrDeposit = ""
        what = type
        print(type)

    money_writer.writerow([date,withdrawOrDeposit,what,amount,balance])

money_writer.writerow(["-------------","-----------------------------------------------","-----------------------------------------------","-------------"])
money_writer.writerow(["Total","",total])
print("Total: ",total)
###########################