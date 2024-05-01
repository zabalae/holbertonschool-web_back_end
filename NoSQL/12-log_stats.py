#!/usr/bin/env python3
'''script that provides some stats about Nginx logs'''


from pymongo import MongoClient


if __name__ == "__main__":
    '''logs stats about Nginx logs'''
    client = MongoClient('mongodb://localhost:27017/')
    collection = client.logs.nginx

    total_logs = collection.estimated_document_count()

    print(f'{total_logs} logs')

    METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')

    for method in METHODS:
        methods_count = collection.count_documents({'method': method})
        print(f'\tmethod: {method}: {methods_count}')

    status_check = collection.count_documents(
        {'method': 'GET', 'path': "/status"})

    print(f"{status_check} status check")
