#!/usr/bin/env python3
"""COMMENT"""

def update_topics(mongo_collection, name, topics):
    """
    Inside of Function
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
