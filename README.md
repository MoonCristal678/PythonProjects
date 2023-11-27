# PythonProjects
### Overview:

This Python script performs several operations related to data manipulation and file handling. It includes functions to create directories, write sets and numbers to files, perform set operations (intersection, difference, union), flatten nested tuples, and generate files containing even numbers and their squared values within specified ranges.

### Functions:

#### 1. `create_directory(directory)`:

- Creates a directory if it does not already exist using the `os.makedirs()` function.

#### 2. `write_set_to_file(team, filename)`:

- Writes the elements of a set (`team`) to a file (`filename`) in the format "Player name: {player}".

#### 3. `teams()`:

- Creates three teams (basketball, baseball, soccer) as sets of player names.
- Calls `write_set_to_file()` to write each team to a corresponding file.
- Performs set operations (intersection, difference, union) on the teams and writes the results to separate files.

#### 4. `flatten_tuple()`:

- Defines a nested tuple and flattens it, writing the flattened result to a file named "flattenTuple.txt".

#### 5. `get_range()`:

- Takes user input for a minimum and maximum number to define a range.

#### 6. `write_numbers_to_file(numbers, filename)`:

- Writes a list of numbers to a file in the format "Number: {num}".

#### 7. `number_even(min_range, max_range)`:

- Generates a list of even numbers within a specified range and writes them to a file named "evenNumbers.txt".

#### 8. `squared_numbers(min_range, max_range)`:

- Generates two lists: regular numbers and their squared values within a specified range.
- Writes pairs of numbers and their squared values to a file named "squaredNumbers.txt".

### How to Use:

1. Run the script.
2. The `teams()` function will create teams and perform set operations, generating files with the results.
3. The `flatten_tuple()` function will flatten a nested tuple and write the result to "data/flattenTuple.txt".
4. The `number_even()` function will prompt for a range and generate even numbers within that range, writing them to "data/evenNumbers.txt".
5. The `squared_numbers()` function will prompt for another range, generate regular and squared numbers, and write them to "data/squaredNumbers.txt".

### Additional Notes:

- The script organizes files within a "data" directory.
- Input validation is not extensively implemented, assuming correct user input for simplicity.
- Each function performs a specific task, and the script demonstrates a variety of file handling and data manipulation techniques.
