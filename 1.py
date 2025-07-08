'''
Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:

If i is a multiple of both 3 and 5, print FizzBuzz.

If i is a multiple of 3 (but not 5), print Fizz.

If i is a multiple of 5 (but not 3), print Buzz.

If i is not a multiple of 3 or 5, print the value of i.

'''
def FizzBuzz(i):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

n=int(input("Enter a number : "))
for i in range(1,n+1):
    (FizzBuzz(i))

'''
output:
Enter a number : 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''