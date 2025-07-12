#!/usr/bin/env python3
"""Comment""" 

def schools_by_topic(mongo_collection, topic):
    """
   Inside of Function 
    """
    return list(mongo_collection.find({"topics": topic}))i
