# Implementation sequence Collatz

def collatz(number):
    print(str(number))
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1

num = int(input("Enter number: "))
while True:
    num = collatz(num)
    if num == 1:
        print("1")
        break
