sen1 = input("Enter a sentence: ")

count_word = sen1.split( )
print(f"The number of words in the sentence is: {len(count_word)}")


#Challenge 1
""" number = int(input("Enter a number: "))
print("Even" if number % 2 == 0 else "Odd") """

#Challenge 2
""" bill = input("How was the service today? (great, good, fair, bad): ")

tip_mapping = {
    "great": "25%",
    "good": "20%",
    "fair": "15%",
    "bad": "0%"
}

tip = tip_mapping.get(bill, "Invalid input")
print(f"Your tip is {tip} please") """

#Challenge 3
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

#Challenge 4
""" import math

def gcf(number1, number2):
    return math.gcd(number1, number2)

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

gcf= gcf(number1, number2)
print("The GCF is: ", gcf) """

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

def gcf(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1

gcf_value = gcf(number1, number2)
print(f"The GCF of {number1} and {number2} is: {gcf_value}")