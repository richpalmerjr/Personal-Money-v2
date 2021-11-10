import os
import csv
import categories

# set the working directory to know where to read the file and write to the CSV file
os.chdir(r"C:\Users\richp\OneDrive\Desktop\Python Projects\Money 2.0")

# setup the variables
textFile = "ReadThisFile.txt"
textFile = open(textFile,"r")
csvFile = open("Money.csv","w",newline="")
money_writer = csv.writer(csvFile, delimiter=",")
totalSpent=float(0)
totalIncome=float(0)
startingBalance=float(0)
currentBalance=""
totalIncome=float(0)
listOfEverything=[]
listOfCategories = categories.dictionary.keys()

###########################
# loop on the text file (bank statement)
for x in textFile:

    # split the lines into an array split by tab
    line = x.split("\t")
    # replace new line characters
    date = line[0].replace("\n","")
    description = line[1].replace("\n","")
    # replace dollar signs ($) and commas with nil so a float can be created
    amount = float(line[2].replace("$","").replace(",","").replace("\n",""))
    balance = float(line[3].replace("$","").replace(",","").replace("\n",""))

    if currentBalance == "":
        currentBalance = balance

    # split the description line if there's a dash, else do not split the line
    # this is just to get if the line is a deposit or not
    if " - " in description:
        withdrawOrDeposit = description.split(" - ")[0]
        what = description.split(" - ")[1]
    else:
        withdrawOrDeposit = ""
        what = description

    category = ""
    # add up the totals and setup the category of each line
    if "Credit" in withdrawOrDeposit or "Deposit" in withdrawOrDeposit:
            totalIncome = totalIncome + amount
            category = "Income"
    else:
            category = ""
            totalSpent = totalSpent + amount
            # get the category of the line
            for x in listOfCategories:
                if x in what:
                    category = categories.dictionary[x]
            #end for
            if category == "":
                category = "Other"

    # save everything to the list, which will get added to the CSV at the end
    listOfEverything.append([category,date,withdrawOrDeposit,what,amount,balance])

# end for
###########################

# set the Starting Balance with the current balance, this is because the list of
# transactions in the bank statement is from most current, to least current
startingBalance = balance

# sort the list of everything
listOfEverything.sort()

# write everything to the csv file
for x in listOfEverything:
    money_writer.writerow(x)

# write the totals to the csv file
money_writer.writerow(["-------------","-------------","-----------------------------------------------","-------------"])
money_writer.writerow(["Total Spent","","",totalSpent])
money_writer.writerow(["Total Income","","",totalIncome])
money_writer.writerow(["Income Left","","",(totalIncome-totalSpent)])

# write the totals to the screen
print("#########################################")
print("Current Balance:\t",currentBalance)
print("Staring Balance:\t",startingBalance)
print()
print("Total Spent:\t",totalSpent)
print("Total Income:\t",totalIncome)
print("")
print("Income Left:\t",(totalIncome-totalSpent))
print("#########################################")