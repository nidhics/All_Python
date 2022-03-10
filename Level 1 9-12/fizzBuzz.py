a=True
while(a):
#Enter a number using custom input
    n = int(input("Enter a nmber: "))

# if number is divisible by both 3 and 5 it returns fizzbuzz
    if (n%5 == 0 and n%3 == 0):
        print("FizzBuzz")

# if number is divisible by 3 it returns fizz
    elif(n%3 == 0 ):
        print("Fizz")

# if number is divisible by 5 it returns buzz
    elif (n%5 == 0):
        print("Buzz")

# if none then simply return the number
    else:
        print(n)
     