#In this file data writing and reading features are incorporated. 

import datetime
import pandas as pd
def readFile(filename):
    
    for line in reversed(list(open(filename))):
        print(line.rstrip())



def writeFile(filename):
    myfile = open (filename, 'w')
    print (filename, " is opened to write file header")
    myfile.write ("Date, Description, Income, Expenditure \n")

    myfile.close()
 
def appendFile(filename):
    today= datetime.datetime.today()
    try:
        description= input("Description: ")
    except SyntaxError:
        description = None
    try:
        income = input("Income: ")
    except SyntaxError:
        income = 0
    try:
        expenditure = input("Expenditure: ")
    except SyntaxError:
        expenditure=0

    with open(filename, 'a') as myfile:
        myfile.write ("{}, {}, {}, {} \n".format(today, description, float(income), float(expenditure)))

def summaryCalculater(filename):
    col_names = ["Date", "Description", "Income", "Expenditure"]
    df= pd.read_csv(filename, sep=',',header=0, index_col=None, names= col_names)
    
    rows= df.shape[0]
    cols =df.shape[1]
    #print ("Rows: ", rows, " Cols: ",cols)
    print ("Total data entries : ", rows)
    #To print a particular row column
   # print(df.iloc[1,3])
    #Create a list of single column with given header 
    income = df["Income"]
    expenditure = df["Expenditure"]
 
    total_income= sum(income)
    total_expenditure = sum(expenditure)
    saving= total_income-total_expenditure
    #Print total income, expenditure and savings to the date
    print ("To the date INCOME: ", total_income, " EXPENSE:",total_expenditure, " SAVING: ", saving)
    print ()
