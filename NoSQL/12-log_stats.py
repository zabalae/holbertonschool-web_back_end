#!/usr/bin/env python3
'''script that provides some stats about Nginx logs'''


from pymongo import MongoClient


if __name__ == "__main__":
    '''logs stats about Nginx logs'''
    client = MongoClient('mongodb://127.0.0.1:27017/')
    collection = client.logs.nginx

    print(f'{collection.count_documents({})} logs')

    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        methods_count = collection.count_documents({'method': method})
        print(f"\tmethod: {method}: {methods_count}")

    status_check = collection.count_documents(
        {'method': 'GET', 'path': "/status"})

    print(f"{status_check} status check")
