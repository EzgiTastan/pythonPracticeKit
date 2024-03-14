# You are going to write a program that calculates the sum of all the even numbers from 1 to X.
# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

target = int(input()) # Number between 0 and 1000
even_sum = 0

for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)