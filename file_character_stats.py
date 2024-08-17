#Samuel Awud
#March 7, 2023

# This function takes in a file name as a parameter, opens the file, reads its content
# and returns the total number of characters in the file.
def count_chars(file_name):
    with open(file_name) as fileobj:
        content = fileobj.read()
        return len(content)
    

# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of alphabetic characters (a to z, A to Z) in the text.
def count_letters(content):
    count = 0
    for char in content:
        if char.isalpha():
            count += 1
    return count


# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of consonants (letters that are not vowels) in the text.
def count_consonants(content):
    count = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for char in content:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count

# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of digits (0 to 9) in the text.
def count_digits(content):
    count = 0
    for char in content:
        if char.isdigit():
            count += 1
    return count

# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of whitespace characters (spaces, tabs, newlines) in the text.
def count_whitespace_chars(content):
    count = 0
    for char in content:
        if char.isspace():
            count += 1
    return count
# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of word characters (alphanumeric characters) in the text.
def count_word_chars(content):
    count = 0
    for char in content:
        if char.isalnum():
            count += 1
    return count
# This function takes in a string of text as a parameter, loops through each character in
# the text and counts the number of punctuation characters (specified by a set of characters)
def count_punc_chars(content):
    count = 0
    punctuation_chars = set(['!', '~', '`', '^', '(', ')', '_', '{', '}', '[', ']', '|', '\\', ';', ':', '?'])
    for char in content:
        if char in punctuation_chars:
            count += 1
    return count


# This function takes in a file name as a parameter, opens the file, reads its content
# and calls the various count functions to get statistics about the file. It then prints
# the statistics to the console and writes them to a new file with the same name as the
# original file, but with "Stats" appended to the filename before the file extension.
def get_stats(file_name):
    while True:
        try:
            with open(file_name) as fileobj:
                content = fileobj.read()
                number_of_chars = count_chars(file_name)
                number_of_letters = count_letters(content)
                number_of_consonants = count_consonants(content)
                number_of_digits = count_digits(content)
                number_of_whitespace_chars = count_whitespace_chars(content)
                number_of_word_chars = count_word_chars(content)
                number_of_punc_chars = count_punc_chars(content)
                # prints the result
                print("\nStatistics for source file: {}\n".format(file_name))
                out_stat = "Statistics for source file: {}\n".format(file_name)
                out_stat += "   Characters: {} \n".format(number_of_chars)
                out_stat += "   Letters: {} \n".format(number_of_letters)
                out_stat += "   Consonants: {} \n".format(number_of_consonants)
                out_stat += "   Digits: {} \n".format(number_of_digits)
                out_stat += "   Spaces: {} \n".format(number_of_whitespace_chars)
                out_stat += "   Word characters: {} \n".format(number_of_word_chars)
                out_stat += "   Punctuation: {} \n".format(number_of_punc_chars)
                print(out_stat)
                # creates output file
                out_file_name = file_name.split('.')[0] + 'Stats.txt'
                with open(out_file_name, "w") as out_file:
                    out_file.write(out_stat)
                return
        except FileNotFoundError:
            # error when file not found
            print('\nERROR: File not found.\n')
            file_name = input("Enter file name: ")
            continue

# The main function provides a brief description of what the program does, prompts the
# user for a file name, and calls the get_stats function with the user input.
def main():
    desc = """
        This code is designed to calculate and display various types 
        of characters in a given file. These include letters, consonants, 
        digits, spaces, words, and punctuation.
    """
    print(desc)
    file_name = input("Enter file name: ")
    get_stats(file_name)

if __name__ == '__main__':
    main()
""" I began the assignment by reading the directions and looking at the 
code. I didn't get stuck, but I had difficulty writing the output on a 
separate file. I put the application through its paces 
with several files, and it worked as expected. I discovered the value of writing 
explicit comments and the benefit of altering code without changing its 
function. I'll make sure to better plan my code changes in the future."""
