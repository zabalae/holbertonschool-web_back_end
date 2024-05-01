#!/usr/bin/env python3
'''Function that lists all documents in a collection'''


import pymongo


def list_all(mongo_collection):
    '''list_all function'''
    all_docs = mongo_collection.find()
    for doc in all_docs:
        all_docs.append(doc)

    return all_docs
