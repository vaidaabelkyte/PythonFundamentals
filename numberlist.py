list1 = []
list2 = []
newlist = []
i = 0

print("Enter 5 number for list 1:  ")
while i < 5:
    try:
        listItem = float(input(str(i + 1) + ": "))
        list1.append(listItem)
        i = i + 1

    except ValueError:
        print("Please only enter number values, try again.")
print()
print("Enter 5 number for list 2:  ")
i = 0 
while i < 5:
    try:
        listItem = float(input(str(i + 1) + ": "))
        list1.append(listItem)
        i = i + 1
    
    except ValueError:
        print("Please only enter number values, try again.")

newList = list1 + list2

print()
print("List 1 merged with List 2 : " + str(newList))
print("Sorted List: " + str(sorted(newList)))