import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_set_to_file(team, filename):
    with open(filename, "w") as file:
        for player in team:
            file.write(f"Player name: {player}\n")

def teams():
    create_directory("data")

    basketball_team = {"Michael", "Lebron", "Treyjhon", "Tyreek", "William"}
    baseball_team = {"Gabrielle", "Joseph", "Mercury", "RJ", "Chris", "Miguel", "Kyrie", "Brian", "Lucas"}
    soccer_team = {"Treyjhon", "Joseph", "Chris", "William", "Lucas", "Gabrielle", "Michael", "Issac", "Cameron", "Mateo", "Emery"}

    write_set_to_file(basketball_team, "data/basketball_set.txt")
    write_set_to_file(baseball_team, "data/baseball_set.txt")
    write_set_to_file(soccer_team, "data/soccer_set.txt")

    with open("data/intersection_basketball_soccer.txt", "w") as file:
        intersection = basketball_team & soccer_team
        for player in intersection:
            file.write(f"Player name: {player}\n")

    with open("data/intersection_baseball_soccer.txt", "w") as file:
        intersection = baseball_team & soccer_team
        for player in intersection:
            file.write(f"Player name: {player}\n")

    with open("data/difference_basketball_soccer.txt", "w") as file:
        difference_basketball_soccer = basketball_team - soccer_team
        file.write("Difference from basketball to soccer:\n")
        for player in difference_basketball_soccer:
            file.write(f"Player name: {player}\n")
        
        file.write("\nDifference from soccer to basketball:\n")
        difference_soccer_basketball = soccer_team - basketball_team
        for player in difference_soccer_basketball:
            file.write(f"Player name: {player}\n")

    with open("data/difference_soccer_baseball.txt", "w") as file:
        difference_soccer_baseball = soccer_team - baseball_team
        file.write("Difference from soccer to baseball:\n")
        for player in difference_soccer_baseball:
            file.write(f"Player name: {player}\n")
    
        file.write("\nDifference from baseball to soccer:\n")
        difference_baseball_soccer = baseball_team - soccer_team
        for player in difference_baseball_soccer:
            file.write(f"Player name: {player}\n")

    with open("data/union_basketball_baseball.txt", "w") as file:
        union = basketball_team | baseball_team
        for player in union:
            file.write(f"Player name: {player}\n")

    with open("data/difference_baseball_basketball.txt", "w") as file:
        difference_basketball_baseball = basketball_team - baseball_team
        file.write("Difference from basketball to baseball:\n")
        for player in difference_basketball_baseball:
            file.write(f"Player name: {player}\n")
        
        file.write("\nDifference from baseball to basketball:\n")
        difference_baseball_basketball = baseball_team - basketball_team
        for player in difference_baseball_basketball:
            file.write(f"Player name: {player}\n")

def flatten_tuple():
   
    nested_tuple = (1, 2, (3, 4, (6, 7)))
    flattened = []

    def flatten_recursive(nested):
        for item in nested:
            if isinstance(item, tuple):
                flatten_recursive(item)
            else:
                flattened.append(item)

   
    flatten_recursive(nested_tuple)

    try:
       
        with open("data/flattenTuple.txt", "w") as file:
            file.write(str(tuple(flattened)))
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Flattened tuple successfully written to file.")


def get_range():
    minimum = int(input("Please enter a minimum number for the range: "))
    maximum = int(input("Please enter a maximum number for the range: "))
    return minimum, maximum

def write_numbers_to_file(numbers, filename):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"Number: {num}\n")
    print(f"{filename} successfully written!")

def number_even(min_range, max_range):
    create_directory("data")
    even_numbers = [i for i in range(min_range, max_range + 1) if i % 2 == 0]
    write_numbers_to_file(even_numbers, "data/evenNumbers.txt")

def squared_numbers(min_range, max_range):
    create_directory("data")
    regular_numbers = [i for i in range(min_range, max_range + 1)]
    squared_numbers = [i ** 2 for i in range(min_range, max_range + 1)]
    with open("data/squaredNumbers.txt", "w") as file:
        for reg_num, squared_num in zip(regular_numbers, squared_numbers):
            file.write(f"Number: {reg_num}  Squared: {squared_num}\n")
    print("Squared File successfully written!")



teams()
flatten_tuple()

minimum_even, maximum_even = get_range()
number_even(minimum_even, maximum_even)

minimum_squared, maximum_squared = get_range()
squared_numbers(minimum_squared, maximum_squared)
