# This is a simple pgm that will let you check to see if a word is a palindrome.
#
# A palindrome is a word, phrase, number or sequence of words that reads the same backward as forward
#
# Since Strings are lists of characters, we can get individual letters with an index and compare them.
# We use the positive index value to check letters left to right
# We use a negative version of the index value to check letters right to left (starting from end of word +1 to account
# for 0 starting index)
#
is_word_a_pailindrome = True  # Let's start assuming word is a palindrome until we determine otherwise


# This function can be used to print some extra info about what's going on.
def print_debug_info(current_index, string_to_check):
    print(f'DEBUG:'
          f'\nCurrent index is {current_index} which points to the letter {string_to_check[current_index]} '
          f'moving left to right.'
          f'\n'  # Add a line break
          f'If we add 1 to index and flip number negative, we get {((current_index + 1) * -1)} '
          f'which is the letter {string_to_check[((current_index + 1) * -1)]} moving from right to left.'
          f'\n'  # Add a line break
          f'Assuming it is a palindrome as long as both letters equal. Still a palindrome? '
          f'{(string_to_check[((current_index + 1) * -1)]) == (string_to_check[current_index])}')


# Get the word we want to check if a palindrome from the user
word_to_check = (  # Get the word to check as input
    input('Enter a word you want to check: ')).upper()  # Let's force uppercase so we can safely compare letters

# Iterate through the list of characters
# We start comparing characters from the left AND the right each iteration.
# As long as we get a match between the characters, it's a palindrome
for idx in range(0, len(word_to_check), 1):
    # DEBUG if you want to see how indexes working
    print_debug_info(idx, word_to_check)
    # Compare the 2 letters from start and end
    if word_to_check[idx] != word_to_check[(idx + 1) * -1]:
        is_word_a_pailindrome = False  # Characters aren't the same so we know the word isn't a palindrome

# Print out the final decision
print(f'\nIs the string {word_to_check} a palindrome? {is_word_a_pailindrome}\n')
