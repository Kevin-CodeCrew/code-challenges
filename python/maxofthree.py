# Prompt the user for 3 numbers.
# Define a function maxOfThree() that takes three numbers as arguments and returns the largest of them.
# The function should NOT prompt for input or produce the output. This should be done from the caller code.
#
# Expected input/output:
# Enter the first number: 4
# Enter the second number: 2112
# Enter the third number: 442
# The largest number entered was: 2112

# We need to get 3 numbers from user. Let's go ahead and cast them to integers
first_number = int(input("Please enter a first number: "))
second_number = int(input("Enter a second number: "))
third_number = int(input("Enter a last number: "))

# This function takes 3 numbers as parameters and will return the largest
def maxOfThree(first_num, second_num, third_num):
    largest_number_so_far = first_num # Doesn't matter which we select to start as largest since will compare to all
    # others

    # See if 2nd num bigger than 1st num
    if (second_num>largest_number_so_far):
        largest_number_so_far = second_num # Now it's the current largest number

    # See if 3rd num bigger than 2nd num
    if (third_num > largest_number_so_far):
        largest_number_so_far = third_num # Now it's the current largest number

    # Function done, return what we ended up with as the largest number
    return largest_number_so_far


# Use our largest number function to pick us the largest value
the_largest_number = maxOfThree(first_number, second_number, third_number)
# Print out the final results
print(f'The largest number out of {first_number}, {second_number}, and {third_number} is... {the_largest_number}')
