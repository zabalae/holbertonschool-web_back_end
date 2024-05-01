#!/usr/bin/env python3
'''script that provides some stats about Nginx logs'''


from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats():
    '''logs stats about Nginx logs'''
    client = MongoClient('mongodb://localhost:27017/')
    collection = client.logs.nginx
    total_logs = collection.count_documents({})

    print(f'{total_logs} logs')
    print('Methods:')
    for method in METHODS:
        methods_count = collection.count_documents({"method": method})
        print(f'\tmethod: {method}: {methods_count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )

    print(f'{status_check} status check')


if __name__ == "__main__":
    log_stats()
