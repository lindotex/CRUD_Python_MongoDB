import os
import time
from classes import crud_python
from prettytable import PrettyTable

def clean_terminal():
    print('\033c', end='')
    
loop_on = True

while loop_on == True:
    print('CONTROL SYSTEM')
    print('CRUD WITH PYTHON AND MongoDB')
    print('')
    print('CHOSE YOR OPTION:')
    t = PrettyTable(['NUMBER','ROUTINE'])
    t.add_row(['1','CREATE'])
    t.add_row(['2','DELETE'])
    t.add_row(['3','READ'])
    t.add_row(['4','UPDATE'])
    t.add_row(['5','EXIT'])
    print(t)
    choice = input("Insert the desired routine number (1, 2, 3, 4 ou 5): ")
        
    if choice == '1':
        print(f'Selected option: {choice}... await.')
        time.sleep(2)
        clean_terminal()
        crud_python.create()
        
    if choice == '2':
        print(f'Selected Option: {choice}... await.')
        time.sleep(2)
        clean_terminal()
        crud_python.delete()
        
    if choice == '3':
        print(f'Selected Option: {choice}... await.')
        time.sleep(2)
        set_freeze = True
        clean_terminal()
        while set_freeze:
            crud_python.read()
            print('Would you like to return to the main manu? Y/N')
            get_menu = input()
            if (get_menu == 'Y') or (get_menu== 'y'):
                set_freeze = False
            if (get_menu == 'N') or (get_menu== 'n'):
                print('We are shutting down the system.')
                time.sleep(2)
                set_freeze = False
                loop_on = False  
        clean_terminal()
        
    if choice == '4':
        print(f'Selected Option: {choice}... await.')
        time.sleep(2)
        clean_terminal()
        crud_python.update()
        
    if choice == '5':
        print(f'Selected Option: {choice}... await.')
        time.sleep(2)
        clean_terminal()
        loop_on = False  
    
    if choice not in ['1','2','3','4','5']:
        print(f'Selected Option: {choice}... await.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('.....')
        time.sleep(1)
        print(f'The value {choice} is not a valid option, we are returning you to the main menu...')
        time.sleep(2)
        clean_terminal()

    
print("The system has been finished. May you have a nice day.")

