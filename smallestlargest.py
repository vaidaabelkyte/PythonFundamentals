listSize = []
num = int(input('How many numbers? '))
for n in range(num):
    numbers = int(input('Enter number: '))
    listSize.append(numbers)
print("Heighest number in a list :", max(listSize), "\nSmallest number in a list :", min(listSize))