from dotenv import load_dotenv, find_dotenv
from db.conn import ConnectionMongoDB
import os
from prettytable import PrettyTable



class users:
    # PROTOTYPE
    def __init__(self, name, occupation, salary) -> None:
        return (name, occupation, salary)


    # CRUD - CREATE
    def create():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        
        connection.connect()
        print('Insert the name to be created:')
        name = str(input())
        print(f'Insert the occupation of {name}:')
        occupation = str(input())
        print(f'Insert the salary of {name}:')
        salary = float(input())
        document = {"name":name, "occupation":occupation, "salary":salary}

        connection.insert_document('users',document)
        print(f'{name} has been successfully added to the database!')
        connection.disconnect()

    # CRUD - READ
    def read():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print("")
        connection.quantity_in_collection('users')
        print("")
        results = connection.execute_query("users", {})
        
        
        if results:
                
            t = PrettyTable(['NAME', 'OCCUPATION', 'SALARY'])
            for document in results:
                
                name = document.get("name", "name not found")
                occupation = document.get("occupation", "occupation not found")
                salary = document.get("salary", "salary not found")
                
                t.add_row([f"{name}", f"{occupation}", F"R$ {salary}"])
            
            print(t)
        else:
            print("No document has been found in your collection 'users'.")
        connection.disconnect()

    # CRUD - UPDATE
    def update():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()


        print('Insert the name to be updated:')
        name = str(input())
        print(f'Would you really like to update the data of {name} on your database? Y/N')
        response = str(input())
        print(f'Insert the new occupation of {name}:')
        value = str(input())
        new_data = {"occupation": value}

        if (response == 'y' or response == 'Y'):
            try:
                connection.update_document('users',{"name":name}, new_data)
                print(f'{name} has been successfully update in database!')
            except Exception as e:
                print('! It was not possible to update the data: ', e)
        else:
            print(f'The user by the name {name} has not been found on our database')

        connection.disconnect() 
 
    # CRUD - DELETE
    def delete():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        connection = ConnectionMongoDB(host=db_url)
        connection.connect()
        print('Insert the name of the person to be removed:')
        name = str(input())
        print(f'Would you really like to remove {name} from your database? Y/N')
        response = str(input())

        if (response == 'y' or response == 'Y'):
            try:
                connection.remove_by_name('users',name)
                print(f'{name} has been successfully removed from the database!')
            except Exception as e:
                print(f'It was not possible to remove {name}', e)
        else:
            print(f'The user by the name of {name} could not be removed from the database')
        connection.disconnect()
