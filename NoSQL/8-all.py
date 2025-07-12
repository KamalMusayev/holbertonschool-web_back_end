#!/usr/bin/python3
#Comment

def list_all(mongo_collection):
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())

    return documents
