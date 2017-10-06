word = input("Enter the word:")

def reverse(word):
    reversedWord = []
    currentPos = len(word) - 1 
    endAt = 0

    for letter in word:
        currentLetter = str(word[currentPos])
        reversedWord.append(currentLetter)
        currentPos = currentPos - 1

    return ''.join(reversedWord)

print(str(word) + "  <=== Reversed===>  " + str(reverse(word)))