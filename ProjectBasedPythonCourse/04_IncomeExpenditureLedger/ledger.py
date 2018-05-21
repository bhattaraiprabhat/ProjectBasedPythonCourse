"""
    In this project we present an income expenditure ledger of a user over the
    period of time. 
    Main features of the project includes view, append and edit  ledger. 

    file: ledger.py
"""


import os
import inputOutput
import datetime
def main():
    print_header()

    ledger_options()


def print_header():
    print ()
    print("#######################################################")
    print("############### Income Expenditure Leger ##############")
    print("#######################################################")
    print ()


def ledger_options():
    """
        Checks if file exists or not. If file doesn't exist, then file is
        created. 
        If file already exists there are option of viewing and appending in
        the file.
    """
   
    fname = "incomeExpenditure.txt"
    if not os.path.isfile(fname):
        print(fname, " doesn't exists")
        inputOutput.writeFile(fname)
        print ("Please rerun the program for further options")

    else:
        print(fname, " exists")

        inputOutput.readFile(fname)
    
        print ("Choose one of the options for ledger................")
        option = input("To view enter: [V], to append enter: [A], to exit enter [X]: \n")
        if option.lower()=="v":
            print ("You entered: ",option, " to VIEW ledger ")
            inputOutput.readFile(fname)
            inputOutput.summaryCalculater(fname)


        elif option.lower()=="a":
            print ("You entered: ",option, " to APPEND ledger")
            inputOutput.appendFile(fname) 
            inputOutput.summaryCalculater(fname)

        elif option.lower()=="x":
            print ("You entered: ",option, " to EXIT ledger \nGOOD BYE.......")
            print()
        else:
            print ("You entered: ",option, ". Please  enter a valid option")
            print()







if __name__=="__main__":
    main()
