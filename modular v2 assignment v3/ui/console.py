
import features.list_add as insert
import features.list_modify as modify
import features.list_getNums as get
import features.list_getProperties as prop
import features.list_filter as filter
import features.list_undo as undo
VERSION = '1.4'
#iter 1: created all of the features in 1 file
#iter 2: started modularizing everything and adding checks (and asserts)
#        console input, and validation of input
# iteration 3: improved console UI, and added expressions to complement numbers in the UI
#              added documentation (docstring) and how to use the program
#iteration 4: non-console UI launcher, learned pygui

def parser(v) -> any:
    """
    """
    print("\n                ===========================================================================")
    print("                                           Math Program  v", VERSION)
    answer = input(f"""                ===========================================================================
                Current input: {v}
                Features: 
                            [1] ADD_NUMBERS: Perform addition operations on the array.
                            [2] MODIFY_LIST: Perform modifications on the array.
                            [3] GET_NUMBERS: Perform retrievals based on checks on the array.
                            [4] GET_PROPERTIES: Perform properties operations on the array.
                            [5] FILTER_LIST: Perform filter operations on the list.
                            [6] UNDO: Perform undo operation on most recent action.
                            [7] LIST: Print the current array to the output.
                            [8] QUIT: Quit the program.
                ===========================================================================

                
                Insert a Number (or expression): 
                """)

    if answer == '8': 
        return "exit", []

    operation = ''
    if len(answer)==1:
        if answer == '1' or answer.startswith('add'):
            operation = input("""
                        
                            "add [value]" -> Add a number to the end of the array
                                -> Usage: "add 10", adds 10 to the end of the array
                    
                            "add @[index] [value]" -> Add a number at the specified index
                                -> Usage: "add @1 10", adds 10 at index 1
                    

                                """)
            
        elif answer == '2' or answer.startswith('remove') or answer.startswith('replace'):
                operation = input("""
                        
                            "remove @[index]" -> Removes element from specified index
                                -> Usage: "remove @1", removes element at index 1
                                            "remove @1-5", removes elements between specified index's
                    
                            "replace [old_val] [new_val]" -> Replaces all occurences of old_val with new_val
                                -> Usage: "replace 1 2", replaces all the 1's with 2's
                                            "replace [1,3,5] [5,3]", replaces all occurences of the first array with the 2nd
                    

                                """)
                

        elif answer == '3' or answer.startswith('primes') or answer.startswith('odds'):
                operation = input("""
                            "primes @[start_index] @[stop_index]" -> Gets all prime numbers between index's
                                -> Usage: "primes 1 5"

                            "odds @[start_index] @[stop_index]" -> Gets all odd numbers between index's
                                -> Usage: "odds 1 5"
                        
                                """)
                

        elif answer == '4' or answer.startswith('sum') or answer.startswith('gcd') or answer.startswith('max'):
                operation = input("""
                            "sum @[start_index] @[stop_index]" -> Sum numbers between index's
                                -> Usage: "sum 1 5"

                            "gcd @[start_index] @[stop_index]" -> Gcd of numbers between index's
                                -> Usage: "gcd 1 5"
                    
                            "max @[start_index] @[stop_index]" -> Max of numbers between index's
                                -> Usage: "max 1 5"

                        
                                """)


        elif answer == '5':
                operation = input("""
                            "filter_prime" -> Removes non-prime numbers from list
                            "filter_negative" -> Removes positive numbers from list


                        
                                """)
                
        elif answer == '6' or answer == "undo":
            operation = "undo "
            print("undone")
        elif answer == '7':
            operation = "list "

        else: operation = input("You didn't insert a valid number, try again: ")
        sliced = operation.rsplit(" ")
    else: sliced = answer.rsplit(" ")
    op_list = ["add", "remove", "replace", "primes", "odds", "sum", "gcd", "max", "filter_prime", "filter_negative", "list", "undo"]

    ok = op_list.index(str(sliced[0]))
    if len(sliced)==1: return ok, sliced
    else: return ok, sliced[1:]



def console_run():
    v, last = [0, 1, 2, 3], [[0, 1, 2, 3]]
    while True:
        to_do = parser(v)
        if to_do[0] == "exit":
            break
        op, apply_to = to_do[0], to_do[1]
        apply_string = apply_to[0].replace('@', '')
        singular = '-' not in apply_string
        if not singular:
            sub1, sub2 = map(int, apply_string.split('-'))
        if op == 0:
            last.append(v.copy())
            insert.insert(v, int(apply_to[0].replace('@', '')), int(apply_to[1])) if len(apply_to) > 1 else insert.add(v, int(apply_to[0]))
        elif op == 1:
            last.append(v.copy())
            modify.remove(v, int(apply_string)) if singular else modify.remove(v, sub1, sub2)
        elif op == 2:
            last.append(v.copy())
            

            old_values = [x.strip() for x in apply_to[0].split(',')]
            new_values = [x.strip() for x in apply_to[1].split(',')]

            if all(x.isdigit() for x in old_values) and all(x.isdigit() for x in new_values):
                old_values = [int(x) for x in old_values]
                new_values = [int(x) for x in new_values]
                if len(old_values)==1: old_values = old_values[0]
                if len(new_values)==1: new_values = new_values[0]
                rez = modify.replace(v, old_values, new_values)
                lol = rez.copy()
                v.clear()
                v.extend(lol)
            else: raise ValueError("Only numbers allowed.")


        elif op in [3, 4, 5, 6, 7]:
            print({3: get.prime, 4: get.odd, 5: prop.sum, 6: prop.gcd, 7: prop.max}[op](v, sub1, sub2))
        elif op == 8:
            last.append(v.copy())
            filter.filter_prime(v)
        elif op == 9:
            last.append(v.copy())
            filter.filter_negative(v)
        elif op == 10:
            print("Current input (cmd):", v)
        elif op == 11:
            undo.undo(v, last)


# Usage \ Notes \ Documentation
""" 
Operations:
                    "add [value]" -> Add a number to the end of the array
                          -> Usage: "add 10", adds 10 to the end of the array
               
                    "add @[index] [value]" -> Add a number at the specified index
                          -> Usage: "add @1 10", adds 10 at index 1
               
                    "remove @[index]" -> Removes element from specified index
                          -> Usage: "remove @1", removes element at index 1
                                    "remove @1-5", removes elements between specified index's
               
                    "replace [old_val] [new_val]" -> Replaces all occurences of old_val with new_val
                          -> Usage: "replace 1 2", replaces all the 1's with 2's
                                    "replace [1,3,5] [5,3]", replaces all occurences of the first array with the 2nd
               
                    "primes @[start_index] @[stop_index]" -> Gets all prime numbers between index's
                          -> Usage: "primes 1 5"

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
