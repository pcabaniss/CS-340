from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient.

        # Connection Variables

        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31279
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Successfully connected...")

    # Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            cResult = self.database.animals.insert_one(data)  # data should be dictionary
            
            # Check for success
            if cResult is not None:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD.
    def read(self, data):
        # Verify parameters
        if data is not None:
            query = self.database.animals.find(data, {"_id": False})
            # If query is successful, print a list
            #for a in query:
             #   print(a)
        else:
            query = self.database.animals.find({}, {"_id": False})
           
        return query
            
                
    # Method to implement the U in CRUD
    def update(self, data, new_data):
        # Verify data is not empty
        if data is not None:
            query = self.database.animals.find(data)
            # If query is found, replace it
            if len(new_data) < 2:
                for animals in query:
                    result = self.database.animals.update_one(data, new_data)
                    print(result)
            else:
                result = self.database.animals.update_one(data, new_data)
        else:
            raise Exception("There was a problem updating data.")
            
    
    # Method to implement the D in CRUD
    def delete(self, data):
        # Verify data is valid
        if data is not None:
            query = self.database.animals.find(data)
        else:
            raise Exception("There was a problem with incoming data.")
        # Delete data
        for animals in query:
            result = self.database.animals.delete_one(data)
            print(result)