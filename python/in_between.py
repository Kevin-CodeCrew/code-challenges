# Practice Question 1:
# Get 2 integers from the user
# Write a function that takes the two integers x1 and x2 returns all the integers BETWEEN them.
# Print 'Here are the numbers between:' then all of the numbers one per line between the 2 integers entered.
# Add some data validation so that if x2 is lower than x1 it should return -1 and your code should
# print 'The second number lower than first!'
# Expected input/output:
# Enter the first number: 5
# Enter the second number: 10
# Here are the numbers between:
# 6
# 7
# 8
# 9

# This challenge all about using range. Range can take 0 or 3 parmeters

# Get 2 numbers from the user
first_num = int(input(f'Please enter the 1st number: '))
second_num = int(input(f'Enter a 2nd number greater than the 1st: '))

# Could add a check here
if (second_num <= first_num):
    print('Second number must be greater than the first number!!! Try again.')
else:
    # Loop through and print the number in between
    print(f'Here are the numbers between {first_num} and {second_num}...\n')
    for number in range((first_num + 1), second_num, 1):
        print(number)
