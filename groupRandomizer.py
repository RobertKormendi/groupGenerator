import random
import math
myList = input("Enter a list of names separated by spaces").split()
max = int(input("Enter the max number of names in a group"))

class Group:
    def __init__(self, names):
        self.names = []
    
    def addNames(self, name):
        self.names.append(name)





groups = []
length = len(myList)

if length % max == 0:
    for i in range(0, int(length/max)):
        groups.append(Group([]))
        
    while myList:
        for i in range(0, len(groups)):
            if myList:
                name = random.randint(0, len(myList)-1)
                groups[i].addNames(myList[name])
                myList.pop(name)


else: 
    for i in range(0, math.ceil(length/max)):
        groups.append(Group([]))
    
    while myList:
        for o in range(0, len(groups)):
            if myList:
                name = random.randint(0, len(myList)-1)
                groups[o].addNames(myList[name])
                myList.pop(name)
            else: 
                break



sum = 0
for i in range (0, len(groups)):
    print(len(groups[i].names))
    sum += len(groups[i].names)

print("There are", len(groups), "groups totalling", sum, "people")
