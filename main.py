import time
from controllers.operations import *

def handle_invalid_selection():
    print('Selected option... not valid. Please enter a valid option.')
    time.sleep(2)
    clean_terminal()

def handle_user_actions(loop_on):
    clean_terminal()
    show_users_menu()
    select = input("Select the desired option:")
    user_actions = {
        '1': action_create,
        '2': action_delete,
        '3': lambda: action_read(loop_on),
        '4': action_update,
        '5': clean_terminal
    }
    action = user_actions.get(select, handle_invalid_selection)
    if select == '3':
        loop_on = action()
    else:
        action()
    return loop_on

def handle_instrument_actions(loop_on):
    clean_terminal()
    show_instruments_menu()
    select = input("Select the desired option:")
    instrument_actions = {
        '1': action_create_instrument,
        '2': action_delete_instrument,
        '3': lambda: action_read_instrument(loop_on),
        '4': action_update_instrument,
        '5': clean_terminal
    }
    action = instrument_actions.get(select, handle_invalid_selection)
    if select == '3':
        loop_on = action()
    else:
        action()
    return loop_on

def handle_equipment_actions(loop_on):
    clean_terminal()
    show_equipments_menu()
    select = input("Select the desired option:")
    equipment_actions = {
        '1': action_create_equipment,
        '2': action_delete_equipment,
        '3': lambda: action_read_equipment(loop_on),
        '4': action_update_equipment,
        '5': clean_terminal
    }
    action = equipment_actions.get(select, handle_invalid_selection)
    if select == '3':
        loop_on = action()
    else:
        action()
    return loop_on

loop_on = True

while loop_on:
    clean_terminal()
    show_menu()
    choice = input("Insert the desired routine number (1, 2 OR 3):")
    
    main_actions = {
        '1': lambda: handle_user_actions(loop_on),
        '2': lambda: handle_instrument_actions(loop_on),
        '3': lambda: handle_equipment_actions(loop_on),
        '4': lambda: (action_exit(), print('Exiting the system...'), time.sleep(2))
    }
    
    action = main_actions.get(choice, lambda: (print('Invalid option, returning to the main menu...'), time.sleep(2), clean_terminal()))
    loop_on = action() if choice in main_actions else handle_invalid_selection

print("The system has been finished. May you have a nice day.")
