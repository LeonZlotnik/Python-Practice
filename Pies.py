pies = ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek","Tamale","Steak"]

print('''Welcome to the House of Pies! Here are our pies: 

--------------------------------------------------------
(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak''')


yn = "y"
selected_pies= []

while yn == "y":
    pie = int(input("which pies woul you like: "))
    print(pie)
    print(f"Great! We'll have that {pies[pie-1]} right out for you.")
    selected_pies.append(pies[pie])
    yn = input("Do you want to make another order) (y/n)")

print("I bought: ")
for x in selected_pies:
    print(x)

    

