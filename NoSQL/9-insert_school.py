#!/usr/bin/env python3
#Comment

def list_all(mongo_collection):
    #Check if the collection is None
    if mongo_collection is None:
        return []

    #Retrieve all documents from the collection
    documents = list(mongo_collection.find())

    #Return the list of documents
    return documents

