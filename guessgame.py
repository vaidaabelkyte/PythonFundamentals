import random
import sys

if sys.version_info[0] < 3:
    input = raw_input


def start_guess():
    num = random.randrange(1, 10)
    print("Guess the number in a range 1 to 10? ")

    while True:
        try:
            guess = int(input("Your guess : "))
        except ValueError:
            print("It must be a number between 1 and 10")
            continue
        if guess == num:
            print("Impressive!!!")
            break
        elif not 1 <= guess <= 10:  
            print(format("too low" if guess < 0 else "too heigh"))
        else:
            print(format("too low" if guess < num else "too heigh"))


if __name__ == '__main__':
    start_guess()
    print("End of program.")