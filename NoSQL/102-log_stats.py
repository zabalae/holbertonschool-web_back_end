#!/usr/bin/env python3
'''script that provides some stats about Nginx logs'''


from pymongo import MongoClient


if __name__ == "__main__":
    '''logs stats about Nginx logs'''
    client = MongoClient('mongodb://localhost:27017/')
    collection = client.logs.nginx

    print(f'{collection.count_documents({})} logs')

    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        methods_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {methods_count}")

    status_check = collection.count_documents(
        {'method': 'GET', 'path': "/status"})

    print(f"{status_check} status check")

    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "$ip": "$_id", "count": 1}},
    ])
    print("IPs:")
    for top_ip in ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f"\t{ip}: {count}")
