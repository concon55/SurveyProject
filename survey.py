import json

allResponses = [] #list of dictionaries

while True:
    thisPerson = {} #each person is a dictionary
    userName = input("What is your name? ")
    thisPerson['name'] = userName
    while True: #check if answer is valid
        userAge = input("What is your age? ")
        if userAge.isdigit():
            thisPerson['age'] = userAge
            break
        else:
            print("Your age must be a number.")
    userPlace = input("Where were you born? ")
    thisPerson['birth place'] = userPlace
    allResponses.append(thisPerson)
    print("Thank you for taking this survey")
    print()
    repeat = input("Would you like to take this survey? ")
    if(repeat.lower() != "yes"):
        break

# print(allResponses)

#opens and writes into a json file called data.json
with open('data.json', 'w') as f:
    json.dump(allResponses, f)

#opens the json file and extracts its data
with open('data.json') as f:
    jsonToDict = json.load(f)

    #get average of ages
    sum = 0
    numItems = len(jsonToDict)
    for item in jsonToDict:
        sum+=int(item['age'])
    average = sum/numItems
    print("The average age is: ", average)

    #get all names
    allNames = []
    for item in jsonToDict:
        allNames.append(item['name'])
    print("Everyone who took this survey: ", allNames)
