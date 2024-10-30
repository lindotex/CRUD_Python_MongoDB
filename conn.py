import pymongo
from pymongo import MongoClient

class ConnectionMongoDB:
    pymongo = pymongo
    MongoClient = MongoClient
    
    def __init__(self, host):
        self.host = host
        self.client = None
        self.db = None

    # DB CONNECTION
    def connect(self):
    
        try:
            # Stablish a MongoDB connection
            self.client = pymongo.MongoClient(host=self.host)
            # Select an specific database
            self.db = self.client.get_database('Test')
            print("Successful MongoDB connection stablish.")
        except pymongo.errors.ConnectionFailure as e:
            print("Error connecting MongoDB:", e)

    # DB DISCONNECTION
    def disconnect(self):
        if self.client:
            self.client.close()
            print("MongoDB connection has been finished.")

    # DB QUERY
    def execute_query(self, collection, query):
        if not self.client:
            print("Error: MongoDB could not be reached.")
            return None

        try:
            # Execute a query in specified collection
            results = self.db[collection].find(query)
            return list(results)  # It returns all results as a dictionary list
        except Exception as e:
            print("Error executing the query:", e)
            return None
    
    # DB CREATE    
    def insert_document(self, collection, document):
        if not self.client:
            print("Error: MongoDB has not stablish connection.")
            return

        try:
            # It add a document in a specific collection
            self.db[collection].insert_one(document)
            print("Document successful insert.")
        except Exception as e:
            print("Error trying to insert the document:", e)
    
    # DB READ ALL ELEMENTS
    def get_all_elements_as_table(self, collection):
        if not self.client:
            print("Error: MongoDB has not stablish connection.")
            return None

        try:
            # get all elements from the specified collection 
            results = self.db[collection].find({})
            
            # It converts the results in a DataFrame of Pandas Lib
            df = pd.DataFrame(list(results))
            return df
        except Exception as e:
            print("Error trying to get all elements as a table:", e)
            return None
    
    # DB READ QUANTITY OF ELEMENTS
    def quantity_in_collection(self, collection):
        if not self.client:
            print("Error: MongoDB has not stablish connection")
            return
        
        try:
            number = self.db[collection].count_documents({})
            print(f'Quantity of items in collection: {number} items.')
        
        except Exception as e:
            print("Error trying to get the document:", e)
    
    # DB UPDATE
    def update_document(self, collection, filter, new_values):
        if not self.client:
            print("Error: MongoDB has not stablish connection.")
            return

        try:
            # It Updates the document in collection based on specified filter
            results = self.db[collection].update_many(filter, {"$set": new_values})
            
            # It verifies if the documents were successfully updated
            if results.modified_count > 0:
                print(f"{results.modified_count} documents successfully updated.")
            else:
                print("No document found to be updated.")
        except Exception as e:
            print("Error during document update:", e)    

    # DB DELETE BY NAME
    def remove_by_name(self, collection, name):
        if not self.client:
            print("Error:MongoDB has not stablish connection.")
            return

        try:
            # It removes the document from collection based on specified name
            results = self.db[collection].delete_one({"name": name})
            
            # It verifies if the document has been successfully removed 
            if results.deleted_count > 0:
                print(f"Document '{name}' successfully removed.")
            else:
                print(f"Document '{name}' have not been found.")
        except Exception as e:
            print("Error trying to remove document:", e)
    
    # DB DELETE BY TAG
    def remove_by_tag(self, collection, tag):
        if not self.client:
            print("Error:MongoDB has not stablish connection.")
            return

        try:
            # It removes the document from collection based on specified name
            results = self.db[collection].delete_one({"tag": tag})
            
            # It verifies if the document has been successfully removed 
            if results.deleted_count > 0:
                print(f"Document '{tag}' successfully removed.")
            else:
                print(f"Document '{tag}' have not been found.")
        except Exception as e:
            print("Error trying to remove document:", e)
        
        
    
    
            
        