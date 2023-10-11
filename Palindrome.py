def is_palindrome(input_string):
    # Convert the input to lowercase (for case-insensitive comparison)
    input_string = str(input_string).lower()
    # Remove spaces and special characters from the input string
    cleaned_string = ''.join(e for e in input_string if e.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Get user input
input_value = input("Enter a word or number: ")

# Check if the input is a palindrome
if is_palindrome(input_value):
    print("Palindrome!")
else:
    print("Not a palindrome!")
