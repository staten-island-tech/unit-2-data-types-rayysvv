""" bill = input("How was the service today? (great, good, fair, bad): ")

if (bill == "great"):
    print("Your tip is 25% please")
elif (bill == "good"):
    print("Your tip is 20% please")
elif (bill == "fair"):
    print("Your tip is 15% please")
elif (bill == "bad"):
    print("Your tip is 0% please") """

""" number = int(input("Enter a number: "))

if (number % 2 == 0):
    print("Even")
else:
    print("Odd") """

""" import math

def gcf(number1, number2):
    return math.gcd(number1, number2)

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

gcf= gcf(number1, number2)
print("The GCF is: ", gcf) """

""" import math

number1 = int(input("Enter a number: "))

def find_factors(number1):
    factors = []
    for i in range(1, number1 + 1):
        if number1 % i == 0:
            factors.append(i)
    return factors

factors = find_factors(number1)
print(f"The factors of {number1} are: {factors}") """

sen1 = input("Enter a sentence: ")

count_word = sen1.split( )
print(f"The number of words in the sentence is: {len(count_word)}")
