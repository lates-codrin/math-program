
import features.list_add as insert
import features.list_modify as modify
import features.list_getNums as get
import features.list_getProperties as prop
import features.list_filter as filter
import features.list_undo as undo
import os

VERSION = '1.5'
TITLE = 'Math Program'

def input_parser(v, errors) -> any:
    """A function that parses user input and returns operation_number, and any arguments given by the user.

    Args:
        v (list): The list which will be displayed on every call.
        errors (str): Errors which will be processed and displayed on every call.

    Raises:
        LookupError, ValueError: If something went wrong while processing user input.

    Returns:
        operation_number: The number coresponding to the operation the user chose. (e.g add = 0)
        arguments: The arguments of the operation (can be 1, 2 or none)
    """

    # <-----------> UI ELEMENTS  <----------->
    print("\n\t===========================================================================")
    print('\t\t\t\t', TITLE, " v", VERSION)

    if errors != "None.":
        errors_text = f"\t[!] Errors: {errors}"
    else:
        errors_text = ""
    answer = input(f"""\t===========================================================================\n\tFeatures: \n\t[1] ADD_NUMBERS: Perform addition operations on the array.\n\t[2] MODIFY_LIST: Perform modifications on the array.\n\t[3] GET_NUMBERS: Perform retrievals based on checks on the array.\n\t[4] GET_PROPERTIES: Perform properties operations on the array.\n\t[5] FILTER_LIST: Perform filter operations on the list.\n\t[6] UNDO: Perform undo operation on most recent action.\n\t[7] LIST: Print the current array to the output.\n\t[8] QUIT: Quit the program.\n\t===========================================================================                            
    \tCurrent input: {v}
    {errors_text}
    \tInsert a Number (or expression):""")

    if answer in {'8', 'q', 'quit', 'exit'}:
        return "exit", []

    commands = {
        '1': """\n\t"add [value]" -> Add a number to the end of the array\n\t"add @[index] [value]" -> Add a number at specified index.""",
        '2': """\n\t"remove @[index]" -> Removes element from index\n\t"remove @start-stop" -> Removes range.\n\t"replace old new" -> Replaces old values with new.""",
        '3': """\n\t"primes @start-stop" -> Gets primes in range\n\t"odds @start-stop" -> Gets odd numbers in range.""",
        '4': """\n\t"sum @start-stop" -> Sum in range\n\t"gcd @start-stop" -> Gcd in range\n\t"max @start-stop" -> Max in range.""",
        '5': """\n\t"filter_prime" -> Removes non-primes\n\t"filter_negative" -> Removes positives.""",
        '6': "undo",
        '7': "list"
    }

    # <-----------> START PARSING DATA  <----------->
    if len(answer) == 1 and answer in commands:
        if answer in ['6', '7']:
            operation = commands[answer]
        else:
            operation = input(commands[answer])
    else:
        operation = answer

    operation_args = operation.split()
    operation_list = ["add", "remove", "replace", "primes", "odds", "sum", "gcd", "max", "filter_prime", "filter_negative", "list", "undo"]

    if operation_args[0] not in operation_list:
        raise LookupError("Input is not a valid command.")

    operation_number = operation_list.index(operation_args[0])

    if operation_number == 0:
        
        if len(operation_args) == 2 and '@' not in operation_args:
            return operation_number, int(operation_args[1])
        elif len(operation_args) == 3 and '@' in operation_args[1]:
            index = int(operation_args[1][1:])
            value = int(operation_args[2])
            return operation_number, [index, value]
        else:
            raise ValueError("Invalid arguments for add/insert command.")

    elif operation_number == 1:
        if len(operation_args) == 2:
            if '-' in operation_args[1]:
                start, end = map(int, operation_args[1][1:].split('-'))
                return operation_number, [start, end]
            elif '@' in operation_args[1]:
                index = int(operation_args[1][1:])
                return operation_number, index
        raise ValueError("Invalid arguments for remove command.")

    elif operation_number == 2:
        if len(operation_args) == 3:
            old_values = [x.strip() for x in operation_args[1].split(',')]
            new_values = [x.strip() for x in operation_args[2].split(',')]
            print(operation_number, old_values, new_values)

            if all(x.isdigit() or x[0] == '-' for x in old_values) and all(x.isdigit() or x[0] == '-' for x in new_values):
                old_values = [int(x) for x in old_values]
                new_values = [int(x) for x in new_values]
                print("arrived")
                return operation_number, [old_values, new_values]
            else: print(all(x.isdigit() or x[1] == '-' for x in old_values) and all(x.isdigit() or x[1] == '-' for x in new_values))
        else: raise ValueError("Invalid arguments for replace command.")

    elif operation_number in [3, 4, 5, 6,7]:
        if len(operation_args) == 3 and '@' in operation_args[1] and '@' in operation_args[2]:
            start = int(operation_args[1][1:])
            end = int(operation_args[2][1:])
            return operation_number, [start, end]
        raise ValueError("Invalid arguments for range-based command.")

    elif operation_number in [8, 9]:
        return operation_number, []

    elif operation_number == 10:
        return operation_number, []

    elif operation_number == 11:
        return operation_number, []

    else:
        raise ValueError("Unexpected operation number or invalid arguments.")


def save_list(current_list:list, last:list):
    """A function that appends current_list to last.

    Args:
        current_list (list): The list we want to append.
        last (list): The list we append to.
    """
    last.append(current_list.copy())

def update_menu():
    """A function that retrieves user input from the input_parser function and runs each operation accordingly, while updating the menu.
    """
    current_list, last, errors = [-1,-2,3,4,5,6,-1,2,-5,-6,-5,2,6,2,9,8,7,-7,6], [[]], "None."
    while True:
        os.system('cls||clear')
        try:
            user_input = input_parser(current_list, errors)
            errors = "None."
        except (LookupError, ValueError) as err:
            errors = str(err) + "Try again!"
            continue
        try:
            operation_number, operation_arguments = user_input[0], user_input[1]
            # <------------>  ADD TO LIST <------------>
            if operation_number == 0:
                save_list(current_list, last)
                if type(operation_arguments) != list: insert.add(current_list, operation_arguments)
                else:
                    index, value = operation_arguments[0], operation_arguments[1]
                    insert.insert(current_list, index, value)
            # <------------> INSERT INTO LIST <------------>
            elif operation_number == 1:
                save_list(current_list, last)
                if type(operation_arguments) == list: 
                    start_index, stop_index = operation_arguments[0], operation_arguments[1]
                    modify.remove(current_list, start_index, stop_index)
                else: modify.remove(current_list, operation_arguments)
            # <------------> REPLACE VALUES IN LIST <------------>
            elif operation_number==2:
                save_list(current_list, last)
                current_list = modify.replace(current_list, operation_arguments[0], operation_arguments[1])
            # <------------> GET PRIMES, ODDS, SUM, GCD, MAX <------------>
            elif operation_number in [3, 4, 5, 6, 7]:
                start_index, stop_index = operation_arguments[0], operation_arguments[1]
                print({3: get.prime, 4: get.odd, 5: prop.sum, 6: prop.gcd, 7: prop.max}[operation_number](current_list, start_index, stop_index))
            # <------------> REMOVE NON PRIMES <------------>
            elif operation_number == 8:
                save_list(current_list, last)
                current_list = filter.filter_prime(current_list)
            # <------------> REMOVE POSITIVE VALUES <------------>
            elif operation_number == 9:
                save_list(current_list, last)
                current_list = filter.filter_negative(current_list)
            # <------------> DISPLAY LIST <------------>
            elif operation_number == 10: print("Current list (ran from cmd):", current_list)
            # <------------> UNDO LAST ACTION <------------>
            elif operation_number == 11: undo.undo(current_list, last)
            # <------------> EXIT THE PROGRAM <------------>
            elif operation_number == "exit": break
        except Exception as err: errors = str(err) + "Try again!"; continue

def console_menu():
    update_menu()

# Usage \ Notes \ Documentation
""" 
[!] [!] [!] OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED OUTDATED [!] [!] [!] 
Operations:
                    "add [value]" -> Add a number to the end of the array
                          -> Usage: "add 10", adds 10 to the end of the array
               
                    "add @[index] [value]" -> Add a number at the specified index
                          -> Usage: "add @1 10", adds 10 at index 1
               
                    "remove @[index]" -> Removes element from specified index
                          -> Usage: "remove @1", removes element at index 1
\t        "remove @1-5", removes elements between specified index's
               
                    "replace [old_val] [new_val]" -> Replaces all occurences of old_val with new_val
                          -> Usage: "replace 1 2", replaces all the 1's with 2's
\t        "replace [1,3,5] [5,3]", replaces all occurences of the first array with the 2nd
               
                    "primes @[start_index] @[stop_index]" -> Gets all prime numbers between index's
                          -> Usage: "primes @1~5"

                    "odds @[start_index] @[stop_index]" -> Gets all odd numbers between index's
                          -> Usage: "odds 1 5"
               
                    "sum @[start_index] @[stop_index]" -> Sum numbers between index's
                          -> Usage: "sum 1 5"

                    "gcd @[start_index] @[stop_index]" -> Gcd of numbers between index's
                          -> Usage: "gcd 1 5"
               
                    "max @[start_index] @[stop_index]" -> Max of numbers between index's
                          -> Usage: "max 1 5"

                    "filter_prime" -> Removes non-prime numbers from list
                    "filter_negative" -> Removes positive numbers from list


"""
'''
lab3
def test_funct1() ...
def func(1)....

test_func(1)

test(gcd())
    assert(gcd(5,10)==5)

'''