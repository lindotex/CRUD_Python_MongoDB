from classes.users import users
from classes.instruments import instruments
import time
from prettytable import PrettyTable

# SERVER METHODS
def clean_terminal():
    print('\033c', end='')

def operation(operator):
    switch = {
       1: "users",
       2: "instruments",
       3: "exit"
    }

def users_operations(operator):
    switch = {
        1: "create",
        2: "read",
        3: "update",
        4: "delete"
    }
    
def instruments_operations(operator):
    switch = {
        1: "create",
        2: "read",
        3: "update",
        4: "delete"
    }
    

# MENUS
def show_menu():
    print('CONTROL SYSTEM')
    print('CRUD WITH PYTHON AND MongoDB')
    print('')
    print('CHOSE YOR OPTION:')
    t = PrettyTable(['NUMBER','ROUTINE'])
    t.add_row(['1','USERS'])
    t.add_row(['2','INSTRUMENTS'])
    t.add_row(['3','EXIT'])
    print(t)

def show_users_menu():
    print('USERS MENU')
    t = PrettyTable(['NUMBER', 'ROUTINE'])
    t.add_row(['1', 'CREATE'])
    t.add_row(['2', 'DELETE'])
    t.add_row(['3', 'READ'])
    t.add_row(['4', 'UPDATE'])
    t.add_row(['5', 'BACK'])
    print(t)
    
def show_instruments_menu():
    print('INSTRUMENTS MENU')
    t = PrettyTable(['NUMBER', 'ROUTINE'])
    t.add_row(['1', 'CREATE'])
    t.add_row(['2', 'DELETE'])
    t.add_row(['3', 'READ'])
    t.add_row(['4', 'UPDATE'])
    t.add_row(['5', 'BACK'])
    print(t)
    
def action_exit():
    print('Selected Option: 3... await.')
    time.sleep(2)
    clean_terminal()



# USERS - CRUD
def action_create():
    print('Selected option: 1... await.')
    time.sleep(2)
    clean_terminal()
    users.create()

def action_delete():
    print('Selected Option: 2... await.')
    time.sleep(2)
    clean_terminal()
    users.delete()

def action_read(loop_on):
    print('Selected Option: 3... await.')
    time.sleep(2)
    clean_terminal()
    set_freeze = True
    while set_freeze:
        users.read()
        print('Would you like to return to the main menu? Y/N')
        get_menu = input()
        if get_menu in ['Y', 'y']:
            set_freeze = False
        elif get_menu in ['N', 'n']:
            print('We are shutting down the system.')
            time.sleep(2)
            set_freeze = False
            loop_on = False
    clean_terminal()
    return loop_on

def action_update():
    print('Selected Option: 4... await.')
    time.sleep(2)
    clean_terminal()
    users.update()



# INSTRUMENTS - CRUD
def action_create_instrument():
    print('Selected option: 1... await.')
    time.sleep(2)
    clean_terminal()
    instruments.create()

def action_read_instrument(loop_on):
    print('Selected Option: 3... await.')
    time.sleep(2)
    clean_terminal()
    set_freeze = True
    while set_freeze:
        instruments.read()
        print('Would you like to return to the main menu? Y/N')
        get_menu = input()
        if get_menu in ['Y', 'y']:
            set_freeze = False
        elif get_menu in ['N', 'n']:
            print('We are shutting down the system.')
            time.sleep(2)
            set_freeze = False
            loop_on = False
    clean_terminal()
    return loop_on
    
def action_update_instrument():
    print('Selected Option: 3... await.')
    time.sleep(2)
    clean_terminal()
    instruments.update()

def action_delete_instrument():
    print('Selected Option: 4... await.')
    time.sleep(2)
    clean_terminal()
    instruments.delete()