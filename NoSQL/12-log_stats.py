#!/usr/bin/env python3
'''script that provides some stats about Nginx logs'''


from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats():
    '''logs stats about Nginx logs'''
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})

    method_counts = {method: collection.count_documents({"method": method}) for method in METHODS}

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in METHODS:
        print(f"    method {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()