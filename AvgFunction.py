
def Average(lst):
    return sum(lst) / len(lst)
    
lst = [2,4,5,7,8,10,14,15,18,19,22,25,26]
average = Average(lst)

print("Your list numbers are: " )

for l in lst:
    print(l)

print("The Average of the list = ", round(average,2))