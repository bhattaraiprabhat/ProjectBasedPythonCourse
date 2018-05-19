#In this game program provides a random number (mostly integer). The game is
#guess the number.   Program gives feedback if the number you chose is lower
#higher than the number provided by the program. 

#This program uses number of basic features in python like random number,
#conditionals (like if, elif, else), string to int conversion and vice-versa. 

#Libraries:
import random

print ("###########################################")
print ("########### Guess a Number  ###############")
print ("###########################################")
print ()

lower_limit =5
upper_limit =95
a_number = random.randint(lower_limit,upper_limit)

done= False
attempt_count= 0
while done==False:
    #Note how to increment counter by one
    attempt_count+=1
    #Note that guess_a_number is a string. 
    guess_a_number= input ("Guess a number between " + str(lower_limit) + " and " \
            + str(upper_limit)+ " :  ")
    #convert string to integer
    guess_a_number_in_int = int(guess_a_number)

    #note a back-slash(\) at the end of line to write in new line
    if guess_a_number_in_int >a_number:
        print ("The number you guessed is "+ str(guess_a_number_in_int) +\
                ": IT IS TOO HIGH!")
    elif guess_a_number_in_int < a_number:
        print ("The number you guessed is "+ str(guess_a_number_in_int) + \
                ": IT IS TOO LOW!")
    else:
        print ("Yeeee! Your guess is right!")
        done= True
print ("Great! You won the game in " + str(attempt_count)+" attempts!")

