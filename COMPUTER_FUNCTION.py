def COMPUTER_FUNCTION(a: int, b:int):
    result = a ^ b
    print(result)

while 1:
    a,b = map(int,input("Please enter the 2 Integers seperated by a comma(eg. 10,20): ").split(","))
    COMPUTER_FUNCTION(a,b)