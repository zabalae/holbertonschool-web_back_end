#!/usr/bin/env python3
'''function that changes all topics on a school document
based on the name'''


def update_topics(mongo_collection, name, topics):
    '''update_topics function'''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
