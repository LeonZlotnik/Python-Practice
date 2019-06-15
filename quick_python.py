#name = "Leon";
#country = "Deutchland";
#age = 26;
#hourly_wage = 7;
#satisfied = True;
#daily_wage = hourly_wage + 8;

#print (f"El daily wage de es {daily_wage}.");


# Conditionals, Paper, Rock, cissors

import random


print("Let's Play Rock Paper Scissors!")


options = ["r", "p", "s"]


computer_choice = random.choice(options)


user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

if (user_choice == "r") and (computer_choice == "p"):
     print ("Computer Won");
     
elif (user_choice == "p") and (computer_choice == "r"):
    print ("You Win!");
    
elif (user_choice == "s") and (computer_choice == "r"):
    print ("Computer Won");
    
elif (user_choice == "r") and (computer_choice == "s"):
    print ("You Win!");
    
elif (user_choice == "p") and (computer_choice == "s"):
    print ("Computer Won");  

elif (user_choice == "s") and (computer_choice == "p"):
    print ("You Win!");

else:
    print ("it's a Tie")
   
   
   
    
# Loops
   
#numbers = [0,1,2,3,4,5,6,7,8,9,10];

#user = input("How many numbers");

#while (n in numbers < numbers):
    #print n 
    
     


