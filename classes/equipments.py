from dotenv import load_dotenv, find_dotenv
from db.conn import *
import datetime
from time import strftime
import os
from prettytable import PrettyTable


class equipments:
    # PROTOTYPE
    def __init__(self):
        pass
    
    # CRUD - CREATE
    def create():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        
        connection.connect()
        print('Insert the tag of the equipment:')
        tag = str(input())
        print(f'Insert the serial number of {tag}:')
        serial_number = str(input())
        print(f'Insert the description of {tag}:')
        description = str(input())
        print(f'Insert the last date of maintenance {tag}:')
        last_maintenance = float(input())
        print(f'Insert the next date of maintenance {tag}:')
        next_maintenance = datetime(input())
        document = {"tag":tag,"serial_number":serial_number, "description":description, "last_maintenance":last_maintenance, "next_maintenance":next_maintenance}

        connection.insert_document('equipments',document)
        print(f'{tag} has been successfully added to the database!')
        connection.disconnect()
        
    # CRUD - READ
    def read():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print("")
        connection.quantity_in_collection('equipments')
        print("")
        equipments = connection.execute_query("equipments", {})
        
        
        if equipments:
                
            t = PrettyTable(['TAG', 'SERIAL', 'DESCRIPTION','LAST MAINTENANCE','NEXT MAINTENANCE'])
            for equipment in equipments:
                
                tag = equipment.get("tag", "tag not found")
                serial_number = equipment.get("serial_number", "serial not found")
                description = equipment.get("description", "description not found")
                last_maintenance = equipment.get("last_maintenance", "minimum not found")
                next_maintenance = equipment.get("next_maintenance", "maximum not found")
                
                t.add_row([f"{tag}", f"{serial_number}",f"{description}", f"{strftime(last_maintenance)}", f"{strftime(next_maintenance)}"])
            
            print(t)
        else:
            print("No document has been found in your collection 'equipments'.")
        connection.disconnect()
    
    # CRUD - UPDATE  
    def update():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()


        print('Insert the tag to be updated:')
        tag = str(input())
        print(f'Would you really like to update the data of {tag} on your database? Y/N')
        response = str(input())
       
        if (response == 'y' or response == 'Y'):
            print(f'Insert the new serial of {tag}:')
            value = str(input())
            new_data = {"serial": value}
            try:
                connection.update_document('equipments',{"tag":tag}, new_data)
                print(f'{tag} has been successfully update in database!')
            except Exception as e:
                print('! It was not possible to update the data: ', e)
                print(f'The equipment with the tag {tag} has not been found on our database')
        else:
            print(f'The equipment with the tag {tag} will not be updated.')
            

        connection.disconnect() 
    
    # CRUD - DELETE
    def delete():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print('Insert the tag of the equipment to be removed:')
        tag = str(input())
        print(f'Would you really like to remove {tag} from your database? Y/N')
        response = str(input())

        if (response == 'y' or response == 'Y'):
            try:
                connection.remove_by_tag('equipments',tag)
                print(f'{tag} has been successfully removed from the database!')
            except Exception as e:
                print(f'It was not possible to remove {tag}', e)
        else:
            print(f'The user by the tag of {tag} could not be removed from the database')
        connection.disconnect()