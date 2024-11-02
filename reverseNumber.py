# Writting code to reverse a number
#Modify the code to set a number to reverse
num = 92536544785868566
#Init variable to store final reverted number
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
#Print the result for the reverted number

print("Reversed Number: " + str(reversed_num))
