#Program that performs the Collatz Sequence

#importing math libary
import math

#Function that calculates collatz sequence for even or odd numbers and returns
#the used formula for given value passed.
def collatz(number):

    if (number % 2) == 0:
        collatz = number // 2
        return print(str(number) + " // 2 =", collatz)
    elif (number % 2) != 0:
        collatz = 3 * number + 1
        return print("3 *", + number, "+ 1 =", collatz)

#Function that calculates collatz sequence for even or odd numbers and returns
#the value found.
def collatzSeq(number):

    if (number < 0):
        raise Exception("Error: Non-positive integer")
        return 

    elif (number % 2) == 0:
        collatz = number // 2
        return collatz

    elif (number % 2) != 0:
        collatz = 3 * number + 1
        return collatz

def main():

        try:
            num = int(input())
        except:
            print("Error: Non-integer value")
            return

        seq = collatzSeq(num)
        if seq == 1:
            print(seq)
        else:
            print(seq)
            #loop that calculates every value until it reaches 1.
            while seq != 1:
                seq = collatzSeq(seq)
                print(seq)
        print("Hasta la vista, baby")
        return

main()
