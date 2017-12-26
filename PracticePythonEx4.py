# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def finddivisors(num):
    """Divisors for the number num"""
    print("Finding divisors of the number ", num)
    divisors=[]
    for i in range (1,num):
        if num%i == 0:
            divisors.append(i)
    if num==0:
            print("Number {} has no divisors", num)
    for div in divisors:
        print(div)


print ("Enter the no. you want to find divisors for")
number = int(input())
print ("You entered :" + str(number))
finddivisors(number)