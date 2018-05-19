#In this project we apply date and time feature of python to compare birth
#dates between two persons. 

#We make the program modular so that it is easy to understand, implement and
#debug. 

#Required Library

import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta



def print_Header():
    print ("#######################################")
    print ("###   Whose Birthday Party First!  ####")
    print ("#######################################")
    print ()

def import_BirthDay(index):
    if index==1:
         print ("Enter your birthday: ")
    else:
         print ("Enter your friend's birthday: ")
     
    birth_year = int(input("Birth Year [YYYY] : "))
    birth_month = int(input("Birth Month [MM] : "))
    birth_day = int(input("Birth Day [DD] : "))
    birth_hour = int(input("Birth Hour [HH] : "))
    birth_min = int(input("Birth Min [MM] : "))
    birth_sec = int(input("Birth Sec [SS] : "))

    return datetime(birth_year, birth_month, birth_day, birth_hour,birth_min,birth_sec)


def calculate_Age(bDay):
    now = datetime.today()
    deltaTime = now-bDay
    
    return deltaTime


def calculate_Birthday_Difference(bDay1, bDay2):
    deltaT= bDay1-bDay2
    
    if deltaT.days<0:
        print ("I am "+ str(round(-deltaT.total_seconds()/(60*60*24*365.25),2)) \
                + " years older than my friend")
    else:

        print ("You friend is "+
                str(round(deltaT.total_seconds()/(60*60*24*365.25),2)) \
                        + " years older than you")



    #Calculate birthday difference:
    months_diff_between_two= bDay1.month-bDay2.month
    dayss_diff_between_two= bDay1.day-bDay2.day

    if months_diff_between_two>0:
        print ("Your birthday is after " +str(months_diff_between_two) + " months of your friends birth day")
    elif months_diff_between_two<0:
        print ("Your birthday is " +str(-months_diff_between_two) + " months earlier than friends birth day")
    else:
        if dayss_diff_between_two>0:
            print ("Your birthday will come after " +str(dayss_diff_between_two)+ " days of your friends birth day")
        elif dayss_diff_between_two<0:
            print ("Your birthday was" +str(-dayss_diff_between_two)+ " days earlier than friends birth day")
        else:
            print ("You to have same birthday!!!")
 

          
        
    #Now Find when is your birthday.............
    months_diff= bDay1.month-datetime.today().month
    days_diff= bDay1.day-datetime.today().day
 
    print ()
    if months_diff>0:
        print ("Your birthday will come after " +str(months_diff) + " months")
    
    elif months_diff<0:
        print ("Your birthday was before " +str(-months_diff) + " months")
    
    else:
        if days_diff>0:
            print ("Your birthday will come after " +str(days_diff)+ " days")
        elif days_diff<0:
            print ("Your birthday was before " +str(-days_diff)+ " days")
        else:
            print ("Today is your birthday! HAPPY BIRTHDAY")

    print ()
                 
def print_Result():
    pass



def main():
    print_Header()
    your_birth_day= import_BirthDay(1)
    #your_birth_day = datetime(1980, 8, 19, 14,10,0)
    print ("Your birth day: "+str(your_birth_day))
    your_Age= calculate_Age(your_birth_day)
    print ("Your age is: "+str(your_Age))

    friends_birth_day= import_BirthDay(2)
    #friends_birth_day= datetime(1980, 8, 19, 9,20,0)

    print ("Your friend's birth day: "+str(friends_birth_day))
    your_friends_age= calculate_Age(friends_birth_day)
    print ("Your friends age is: "+str(your_friends_age))
    calculate_Birthday_Difference(your_birth_day,friends_birth_day)


if __name__=="__main__":
    main()
