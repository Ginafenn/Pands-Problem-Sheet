#This program asks the user to input any positive integer and outputs the successive values of the following calculation
#https://www.webucator.com/article/collatz-conjecture-in-python/
#author:Regina Fennessy

def collatz(number):
    while number != 1: #
        print(number)
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int(3 * number + 1)
    else:
        print(number)


def main():
    number = int(input('Please enter a positive integer: '))
    collatz(number)
main()