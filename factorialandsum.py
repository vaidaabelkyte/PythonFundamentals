import math

f = input("Enter the number: ")
n = 1

for i in range(1, int(f) + 1): 
    n = n * i           

def result(n):
    currentPos = 0
    digits = []
    result = 0
    answer = str(n)

    print(str(f) + "! = " + str(n))

    for digit in answer:
        currentNum = str(answer[currentPos]) 
        digits.append(currentNum) 
        currentPos = currentPos + 1

  
    for num in digits:
        result = result + int(num)

    return result



print("The sum of  " + str(f) + "! = " + str(result(n)))


f = str (math.factorial (100))
result = 0
for i in f:
    result += int (i)

print("The sum of  100 ! = " + str(result))
