aPerson = {
    'name': "Leon",
    'age': 27,
    'hobbies': ['coding','piano','swimming','singing','biking','cooking']
}

Sleeping = {
    'monday': "7hrs on monday",
    'tuesday': " 7hrs on tuesday",
    'wednesday': " 8 1/2hrs on wednesday",
    'thursday': " 7 hrs on thursday",
    'friday': " 8hrs on friday",
    'saturday':" 8hrs on saturday",
    "sunday":" and on sunday It depends jeje"
}

hobbies = aPerson['hobbies']

print(f"{aPerson['name']} has {aPerson['age']} year old, and his main hobbies are:")

for hobby in hobbies:
    print(hobby)

knowMore = input(f"Would you like more about {aPerson['name']}?(y/n)")

if knowMore == "y":
    print(f"{aPerson['name']} sleeps {Sleeping['monday']},{Sleeping['tuesday']},{Sleeping['wednesday']},{Sleeping['thursday']},{Sleeping['friday']},{Sleeping['saturday']},{Sleeping['sunday']},")
else:
    print("Bye!")