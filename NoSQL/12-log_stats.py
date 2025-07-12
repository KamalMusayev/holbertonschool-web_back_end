#!/usr/bin/env python3
"""Module to provide some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def log_stats():
    """
    Connects to MongoDB logs.nginx collection and prints:
    - Number of logs
    - Number of logs by HTTP method
    - Number of GET /status requests
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
