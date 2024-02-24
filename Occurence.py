import string

def count_word_occurrences(text):
    # Split the text into individual words
    words = text.split()

    # Initialize a dictionary to store word occurrences
    word_count = {}

    # Iterate through each word in the text
    for word in words:
        # Remove special characters and punctuation, and convert to lowercase
        word = word.lower().strip(string.punctuation)

        # Check if the word exists in the dictionary
        if word in word_count:
            # Increment the count if the word exists
            word_count[word] += 1
        else:
            # Add the word to the dictionary with count 1 if it doesn't exist
            word_count[word] = 1

    return word_count

# Getting input from the user
text = input("Enter the text: ")

# Count occurrences of each word in the text
word_occurrences = count_word_occurrences(text)

# Print the result
print("Word occurrences:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
