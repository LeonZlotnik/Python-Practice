#candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
 #            "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

#for candy in candyList:
 #   print (candy,candyList.index(candy)); 

#allowance = input("What is your amount of allowance")

#if allowance == allowance:
 #   for allowance in allowance:
 #       print allowance

candies = ["Snickers","Kit Kat","Sour Patch Kids","Juicy Fruit","Swedish Fish","Skittles","Hershey Bar","Starbursts","M&Ms"]

candySelection = []
for i in range(len(candies)):
    print("[" + str(i)+"]"+ candies[i])

answer = "y"
while answer == "y":
    candyIndex = int(input("Select the candy you would like to take"))
    candy = candies[candyIndex]
    candySelection.append(candy)
    answer = input("Would you like to continue?(y/n)")

    if answer == "n":
        for i in range(len(candySelection)):
            print(candySelection[i])