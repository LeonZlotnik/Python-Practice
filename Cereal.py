import csv

cerealChoice = input("What Cereal do you want ")
foundCereal = False

with open('cereal.csv','r',newline='') as csvfile:
    cerealList = csv.reader(csvfile, delimiter=',')

    for cereal in cerealList:
        if cerealChoice in cereal and cereal[7] > 5:
            foundCereal = True
            break
    
    if foundCereal:
        print (f"{cereal[0]} has {cereal[7]}g of fiber")
    else:
        print ("Not Found")