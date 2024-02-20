# Define a function that counts the number of words in a string
def count_words(text):
  # Split the text by whitespace characters
  words = text.split()
  # Return the length of the words list
  return len(words)

# Prompt the user to enter a sentence or paragraph
print("Please enter a sentence or paragraph:")
text = input()

# Check if the input is empty
if text == "":
  # Display an error message
  print("Error: No input entered.")
else:
  # Call the count_words function and store the result
  word_count = count_words(text)
  # Display the word count
  print(f"The word count is {word_count}.")
