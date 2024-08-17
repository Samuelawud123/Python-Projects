#Samuel Awud
#March 16, 2023

#Opens a file in read mode and returns its content as a list of lines.
#Prompts the user for a valid file name if IOError is encountered.
def open_and_read_file(file_name):
    try:
        with open(file_name, "r") as f:
            return f.readlines()
    except IOError:
        print("Unable to open file, please enter a valid name : ")
        file_name = input()
        return open_and_read_file(file_name)
    
#This function takes a list of keys as an input parameter
#Strips whitespace from each key in a list and returns them
def populate_keys(key_file):
    keys=[]
    for key in key_file:
        keys.append(key.strip())
    return keys
#This function prompts the user to enter a file path for the data file and
# returns the content of the file as a list of lines
def data_path():
    print("Enter data file path: ")
    data_file_path = input()
    lines = open_and_read_file(data_file_path)
    return lines

#Processes the data in the lines according to the keys provided 
# and prints the result for each dataset.
#Calculates the number of datasets and the average number of matches.
def processing(lines,keys):
    line_number = 0
    data_sets = 0
    matches = 0
    current_dataset = ""
    for line in lines:
        line = line.strip()
        if line_number % 2 == 0:
            current_dataset = line
            data_sets += 1
        else:
            data = line.split(",")
            result = []
            current_matches = 0
            for i in range(len(keys)):
                if(keys[i] == data[i]):
                    result.append(True)
                    matches += 1
                    current_matches += 1
                else:
                    result.append(False)
            
            print(current_dataset, result, current_matches)

        line_number += 1

    print("# of Datasets={0} : Average matches={1}".format(data_sets, matches/data_sets))

#Reads keys from "Key.txt".
#Populates keys and prompts user for data file path.
#Processes data using processing() function
def main():
    key_file = open_and_read_file("Key.txt")
    keys=populate_keys(key_file)
    lines=data_path()
    processing(lines,keys)
    
main()
    

'''To solve the assignment, I created three functions to read files, 
populate keys, and prompt the user for data. The main function used 
these functions to process the data, iterate over each line, compare 
values to keys, output results, and calculate the number of matches. 
Testing was done with various input files, and I gained experience in
file I/O and error handling.'''



