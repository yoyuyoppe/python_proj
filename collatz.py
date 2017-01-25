# Implementation sequence Collatz

def collatz(number):
    print(str(number))
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Enter the integer")
    exit()
    
while True:
    num = collatz(num)
    if num == 1:
        print("1")
        break
