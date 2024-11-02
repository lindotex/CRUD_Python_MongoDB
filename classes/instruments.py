from dotenv import load_dotenv, find_dotenv
from db.conn import *
import os
from prettytable import PrettyTable


class instruments:
    def __init__(self):
        pass
    
    # CRUD - CREATE
    def create():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        
        connection.connect()
        print('Insert the tag of the instrument:')
        tag = str(input())
        print(f'Insert the serial number of {tag}:')
        serial_number = str(input())
        print(f'Insert the description of {tag}:')
        description = str(input())
        print(f'Insert the minimum value of the range of {tag}:')
        minimum_value = float(input())
        print(f'Insert the maximum value of the range of {tag}:')
        maximum_value = float(input())
        document = {"tag":tag,"serial_number":serial_number, "description":description, "minimum_value":minimum_value, "maximum_value":maximum_value}

        connection.insert_document('instruments',document)
        print(f'{tag} has been successfully added to the database!')
        connection.disconnect()
        
    # CRUD - READ
    def read():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print("")
        connection.quantity_in_collection('instruments')
        print("")
        instruments = connection.execute_query("instruments", {})
        
        
        if instruments:
                
            t = PrettyTable(['TAG', 'SERIAL', 'DESCRIPTION','MINIMUM','MAXIMUM'])
            for instrument in instruments:
                
                tag = instrument.get("tag", "tag not found")
                serial_number = instrument.get("serial_number", "serial not found")
                description = instrument.get("description", "description not found")
                minimum_value = instrument.get("minimum_value", "minimum not found")
                maximum_value = instrument.get("maximum_value", "maximum not found")
                
                t.add_row([f"{tag}", f"{serial_number}",f"{description}", f"{minimum_value}", f"{maximum_value}"])
            
            print(t)
        else:
            print("No document has been found in your collection 'instruments'.")
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
                connection.update_document('instruments',{"tag":tag}, new_data)
                print(f'{tag} has been successfully update in database!')
            except Exception as e:
                print('! It was not possible to update the data: ', e)
                print(f'The instrument with the tag {tag} has not been found on our database')
        else:
            print(f'The instrument with the tag {tag} will not be updated.')
            

        connection.disconnect() 
    
    # CRUD - DELETE
    def delete():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print('Insert the tag of the person to be removed:')
        tag = str(input())
        print(f'Would you really like to remove {tag} from your database? Y/N')
        response = str(input())

        if (response == 'y' or response == 'Y'):
            try:
                connection.remove_by_tag('instruments',tag)
                print(f'{tag} has been successfully removed from the database!')
            except Exception as e:
                print(f'It was not possible to remove {tag}', e)
        else:
            print(f'The user by the tag of {tag} could not be removed from the database')
        connection.disconnect()