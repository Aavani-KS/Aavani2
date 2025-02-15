# Function to count the number of words in the input text
def count_words(text):
    # Split the text by spaces to get a list of words
    words = text.split()
    
    # Return the length of the list which is the number of words
    return len(words)

# Main function to interact with the user
def main():
    # Ask the user to input a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if user_input.strip() == "":
        print("Error: The input is empty. Please enter something.")
    else:
        # Count the words using the count_words function
        word_count = count_words(user_input)

        # Display the word count
        print(f"The number of words in your input is: {word_count}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
