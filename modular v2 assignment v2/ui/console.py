
import features.list_add as insert
import features.list_modify as modify
import features.list_getNums as get
import features.list_getProperties as prop
import features.list_filter as filter
import features.list_undo as undo
VERSION = '1.3'
# iteration 3: better UI, and added expressions to complement numbers in the UI
def parser(v) -> any:

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



def run():
    v = [0, 1, 2, 3]
    last = []
    last.append(v.copy())
    while True:
        to_do = parser(v)
        print(to_do)
        

        if to_do[0] == "exit":
            print("Exiting program.")
            break
        
        apply_to = to_do[1]
        operation = to_do[0]
        print(f"                Operation: {operation}, Apply to: {apply_to}")
        


        apply_string = apply_to[0]
        singular = True
        if '@' in apply_string:
                    apply_string = apply_string.replace('@', '')

                    if '-' in apply_string:
                        singular = False
                        indices = apply_string.split('-')
                        
                        sub1 = int(indices[0])
                        sub2 = int(indices[1])
                        
        if operation == 0:  # Add operation
            if len(apply_to) > 1:
                last.append(v.copy())
                insert.insert(v, int(apply_to[0].replace('@', '')), int(apply_to[1]))
            else:
                last.append(v.copy())
                insert.add(v, int(apply_to[0]))

        elif operation == 1:
            if len(apply_to) > 0:
                        if singular:
                            sub1 = int(apply_string)  # single index
                            
                            print("Single index:", sub1)
                            last.append(v.copy())
                            modify.remove(v, sub1)
                        else: 
                             last.append(v.copy())
                             modify.remove(v, sub1, sub2)
                
                


        elif operation == 2:
             last.append(v.copy())
             sube1 = apply_to[0].replace('[','').replace(']','')
             sube1 = sube1.rsplit(',')
             sube1 = [int(x) for x in sube1]

             sube2 = apply_to[1].replace('[','').replace(']','')
             sube2 = sube2.rsplit(',')
             sube2 = [int(x) for x in sube2]
             
             modify.replace(v,sube1,sube2)
        elif operation == 3:
             print(get.prime(v, sub1, sub2))
        elif operation == 4:
             print(get.odd(v, sub1, sub2))
        elif operation == 5:
             print(prop.sum(v, sub1, sub2))
        elif operation == 6:
             print(prop.gcd(v, sub1, sub2))
        elif operation == 7:
             print(prop.max(v, sub1, sub2))
        elif operation == 8:
             last.append(v.copy())
             filter.filter_prime(v)
        elif operation ==9:
             last.append(v.copy())
             filter.filter_negative(v)
        elif operation ==10:
             print("                Current input (cmd): ", v)
        elif operation == 11:
             undo.undo(v,last)
             

# replace [1,3,5] [2,5]

# Run the program in a loop

# notes
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