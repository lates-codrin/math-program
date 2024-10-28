import dearpygui.dearpygui as dpg
import features.list_add as insert
import features.list_modify as modify
import features.list_getNums as get
import features.list_getProperties as prop
import features.list_filter as filter
import features.list_undo as undo



    
current_list = []
last_states = [current_list.copy()]


# ================================== INPUT PARSING FUNCTIONS ================================== #
def add_number(sender, app_data, user_data):
        last_states.append(current_list.copy())
        value = dpg.get_value("add_value")
        insert.add(current_list, value)
        update_list_display()

def insert_number(sender):
        last_states.append(current_list.copy())
        index = dpg.get_value("insert_index")
        value = dpg.get_value("insert_value")
        insert.insert(current_list, index, value)
        update_list_display()

def remove_number(sender):
        last_states.append(current_list.copy())
        index = dpg.get_value("remove_index")
        modify.remove(current_list, index)
        update_list_display()

def replace_number(sender):
    last_states.append(current_list.copy())
    result = "Done."

    old_values_str = dpg.get_value("replace_old")
    new_values_str = dpg.get_value("replace_new")
    
    old_values = [x.strip() for x in old_values_str.split(',')]
    new_values = [x.strip() for x in new_values_str.split(',')]
    for x in old_values:
         if not (x.isdigit() or x[0]=='-'): print(x, "no")
    if all((x.isdigit() or x[0] == '-') for x in old_values) and all((x.isdigit() or x[0] == '-') for x in new_values):
        old_values = [int(x) for x in old_values]
        new_values = [int(x) for x in new_values]
        if len(old_values)==1: old_values = old_values[0]
        if len(new_values)==1: new_values = new_values[0]
        if old_values not in current_list:
            dpg.hide_item("replace_window")
            dpg.configure_item("modal_id", show=True)
        else:
            rez = modify.replace(current_list, old_values, new_values)
            lol = rez.copy()
            current_list.clear()
            current_list.extend(lol)
            dpg.set_value("result_text", f"Result: {result}")
            update_list_display()
    else: 
        dpg.hide_item("replace_window")
        dpg.configure_item("modal_id", show=True)


def get_property(sender):
        operation = sender
        start_index = dpg.get_value("start_index")
        end_index = dpg.get_value("end_index")
        
        result = [1]
        if operation == "primes":
            try:
                result = get.prime(current_list, start_index, end_index)
            except IndexError as err:
                 result = err
        elif operation == "odds":
            try:
                result = get.odd(current_list, start_index, end_index)
            except IndexError as err:
                 result = err
        elif operation == "sum":
            try:
                result = prop.sum(current_list, start_index, end_index)
            except IndexError as err:
                 result = err
        elif operation == "gcd":
            try:
                result = prop.gcd(current_list, start_index, end_index)
            except IndexError as err:
                 result = err
        elif operation == "max":
            try:
                result = prop.max(current_list, start_index, end_index)
            except IndexError as err:
                 result = err
        
        dpg.set_value("result_text", f"Result: {result}")

def filter_list(sender):
        filter_type = sender
        last_states.append(current_list.copy())
        result = "Done."
        if filter_type == "prime":
            rez = filter.filter_prime(current_list)
            current_list.clear()
            current_list.extend(rez)
        elif filter_type == "negative":
            rez = filter.filter_negative(current_list)
            current_list.clear()
            current_list.extend(rez)
        dpg.set_value("result_text", f"Result: {result}")
        update_list_display()

def undo_operation(sender):
        if last_states:
            current_list.clear()
            current_list.extend(last_states.pop())
            update_list_display()
def instructions(sender):
        dpg.add_text("ba")

# ================================== UI HELPER FUNCTIONS ================================== #


def update_list_display():
        dpg.set_value("current_list_text", f"Current List: {current_list}")
        dpg.set_value("last_saved_list_text", f"Last-Saved List: {last_states[-1]}" if last_states else "No Saved State")

# ================================== MAIN UI FUNCTION ================================== #
def gui_menu():
    dpg.create_context()
    dpg.set_global_font_scale(1.5)
    dpg.create_viewport(title='Math Program v1.4', width=800, height=600, always_on_top=True)

    with dpg.window(tag ="main_window", label="Math Program v1.4", pos=(0, 0), width=800, height=40, no_resize=True):
        dpg.add_text("Current List: ", tag="current_list_text")
        dpg.add_text("Last-Saved List: ", tag="last_saved_list_text")

        dpg.add_text("Result: ", tag="result_text")
        dpg.set_value("result_text", "Result: Nothing yet!")

        with dpg.menu_bar():
            with dpg.menu(label="Add / Insert |"):
                    dpg.add_menu_item(label="Add Number", callback=lambda: dpg.show_item("add_window"))
                    dpg.add_menu_item(label="Insert Number", callback=lambda: dpg.show_item("insert_window"))
            with dpg.menu(label="Modify |"):
                    dpg.add_menu_item(label="Remove Number", callback=lambda: dpg.show_item("remove_window"))
                    dpg.add_menu_item(label="Replace Number", callback=lambda: dpg.show_item("replace_window"))
                    with dpg.window(label="Error", modal=True, tag="modal_id", no_close=True, autosize=True, show=False, pos=(150,200)):
                        dpg.add_text("Invalid input or value not in list; try again.")
                        dpg.add_button(label="Close", callback=lambda: [dpg.configure_item("modal_id", show=False), dpg.show_item("replace_window")])
            dpg.add_menu_item(label="Get Properties |", callback=lambda: dpg.show_item("properties_window"))
            with dpg.menu(label="Filter |"):
                    dpg.add_menu_item(label="Filter Prime", callback=filter_list, tag = "prime")
                    dpg.add_menu_item(label="Filter Negative", callback=filter_list, tag = "negative")
            with dpg.menu(label="Undo |"):
                    dpg.add_menu_item(label="Undo Last Operation", callback=undo_operation)
            dpg.add_menu_item(label="Help", callback=lambda: dpg.show_item("help_window"))

        # Create windows for each operation and one for errors
        with dpg.window(label="Add Number", modal=True,tag="add_window", show=False, width=780, height=300, pos=[0,300]):
            dpg.add_input_int(label="Value", default_value=10, tag="add_value")
            dpg.add_button(label="Add", callback=add_number)

        with dpg.window(label="Insert Number",modal=True, tag="insert_window", show=False, width=780, height=300, pos=[0,300]):
            dpg.add_input_int(label="Value", default_value=10, tag="insert_value")
            dpg.add_input_int(label="Index", default_value=0, tag="insert_index")
            dpg.add_button(label="Insert", callback=insert_number)

        with dpg.window(label="Remove Number", modal=True,tag="remove_window", show=False, width=780, height=300, pos=[0,300]):
            dpg.add_input_int(label="Index", default_value=0, tag="remove_index")
            dpg.add_button(label="Remove", callback=remove_number)

        with dpg.window(label="Replace Number", tag="replace_window", show=False, width=780, height=300, pos=[0,300]):
            dpg.add_text("Values can be comma-separated.")
            dpg.add_input_text(label="Old Value(s)", default_value="0", tag="replace_old")
            dpg.add_input_text(label="New Value(s)", default_value="0", tag="replace_new")
            dpg.add_button(label="Replace", callback=replace_number)

        with dpg.window(label="Get Properties",modal=True, tag="properties_window", show=False, width=780, height=300, pos=[0,300]):
            dpg.add_input_int(label="Start Index", default_value=0, tag="start_index")
            dpg.add_input_int(label="End Index", default_value=len(current_list), tag="end_index")
            dpg.add_button(label="Get Primes", callback=get_property, tag="primes")
            dpg.add_button(label="Get Odds", callback=get_property, tag="odds")
            dpg.add_button(label="Get Sum", callback=get_property, tag="sum")
            dpg.add_button(label="Get GCD", callback=get_property, tag="gcd")
            dpg.add_button(label="Get Max", callback=get_property, tag="max")

        
        with dpg.window(label="Instructions", no_scrollbar = False, tag="help_window", show=False, width=780, height=300, pos=[0,270]):
            dpg.add_text("""
Operations:

1. Add a Number
- Button: add [value]
- Description: Adds a number to the end of the array.
- Usage:
  - Example: add 10
    - Effect: Adds 10 to the end of the array.

2. Add a Number at a Specific Index
- Button: add @[index] [value]
- Description: Adds a number at the specified index in the array.
- Usage:
  - Example: add @1 10
    - Effect: Adds 10 at index 1.

3. Remove an Element
- Button: remove @[index]
- Description: Removes an element from the specified index.
- Usage:
  - Example 1: remove @1
    - Effect: Removes the element at index 1.
  - Example 2: remove @1-5
    - Effect: Removes elements between index 1 and 5.

4. Replace Values
- Button: replace [old_val] [new_val]
- Description: Replaces all occurrences of old_val with new_val.
- Usage:
  - Example 1: replace 1 2
    - Effect: Replaces all 1's with 2's.
  - Example 2: replace [1,3,5] [5,3]
    - Effect: Replaces all occurrences of the first array with the second.

5. Get Prime Numbers
- Button: primes @[start_index] @[stop_index]
- Description: Retrieves all prime numbers between the specified indices.
- Usage:
  - Example: primes 1 5
    - Effect: Returns all prime numbers between index 1 and 5.

6. Get Odd Numbers
- Button: odds @[start_index] @[stop_index]
- Description: Retrieves all odd numbers between the specified indices.
- Usage:
  - Example: odds 1 5
    - Effect: Returns all odd numbers between index 1 and 5.

""")

            


    update_list_display()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main_window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
