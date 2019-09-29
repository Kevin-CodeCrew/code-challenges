# Exercise 4: Classes
# # Create a program for comparing how many eggs each Hen lays.
#
# Create a Hen class that has the properties name, color, and egg count
# When you run the program, prompt the user for a name a color, and the egg count for the Hen and create a new Hen
# instance
# Let the user create 2 more Hens (for a total of 3)
# Compare the egg counts for the 3 Hen class instances using their properties
# Print the information for the Hen with the highest egg count.
#
# Sample Output:
# # The Hen with the most eggs was... Harriet the Brown Hen with 6 eggs!
#
# All user input *and* output should be handled *outside* of the class!

# The Hen class. Each Hen has a name, a color, and some number of eggs

class Hen:
    def __init__(self, name, color, eggs=0):
        self.name_p = name
        self.color_p = color
        self.eggs_p = eggs

    # Override the to string method and return the Hen's properties
    def __str__(self):
        return f'{self.name_p} the {self.color_p} Hen with {self.eggs_p}!'


# Let's create a list to hold the Hen class instances in
hen_house_list = []
# Let the user create 3 hens (up to but not including 3 since list starts at 0)
for knt in range(3):
    hen_name = input("\nPlease enter the Hen name: ")
    hen_color = input(f"Enter what color {hen_name} is: ")
    hen_number_of_eggs = int(input(f"Enter the number of eggs laid by {hen_name} :"))
    # Now create a new Hen instance with the info we collected
    my_new_hen = Hen(hen_name, hen_color, hen_number_of_eggs)
    # Now add the Hen to our hen house
    hen_house_list.append(my_new_hen)

the_most_eggs = -1  # Start with super low value
hen_with_the_most_eggs_index = -1  # Start with placeholder value

# Let's check each Hen in our hen house list
for idx in range(len(hen_house_list)):
    # print(hen)  # Uncomment to Print Hen's info for DEBUG
    if (hen_house_list[idx].eggs_p > the_most_eggs):
        the_most_eggs = hen_house_list[idx].eggs_p
        hen_with_the_most_eggs_index = idx

# We could also use enumerate to just get the index and value at the same time
# We haven't spent time on this but see if you can figure out how it works!
# for ndx, hen in enumerate(hen_house_list):
#     if (hen.eggs_p > the_most_eggs):
#         the_most_eggs = hen.eggs_p
#         hen_with_the_most_eggs_index = ndx

# When we finish looping through, hen_with_the_most_eggs_index should point to the winning Hen!
print(f'\nAnd the Hen with the most eggs is...\n'
      f'{hen_house_list[hen_with_the_most_eggs_index]}')
