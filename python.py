# # intput three numbers and find the largest one use and if-else ladder
# def largestnumber(numbers):
#     largest=numbers[0]
#     for num in numbers:
#          if num>largest:
#               largest=num
#     return largest
# print(largestnumber([20,40,60,80,100]))


# Write a menu-driven program to perform basic arthmetic operations addition,substraction,multiplication,division

# def add(a, b):
#     return a + b
# print(add(2,5))

# def subtract(a, b):
#     return a - b
# print(subtract(100,50))

# def multiply(a, b):
#     return a * b
# print(multiply(5,5))

# def divide(a, b):
#     if b != 0:
#         return a / b
# print(divide(6,3))
    



# print numbers from 1 to 100.for multiples of 3,print "Fizz".for multiples of 5,print "Buzz",and for multiples of both,print "FizzBuzz"

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

        
# input a number n,and find all its divisors using a loop

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# input a number and count the digits,calculate their sum,and find their product
# num = int(input("Enter a number: "))

# count = 0
# digit_sum = 0
# digit_product = 1

# for digit in str(abs(num)):  
#     count += 1
#     digit_sum += int(digit)
#     digit_product *= int(digit)

# print(count)
# print(digit_sum)
# print(digit_product)

# A number is a perfect number if the sum of its divisors equals 
num = int(input("Enter a number: "))

divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(num)
else:
    print(num)
