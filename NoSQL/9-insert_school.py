#!/usr/bin/env python3
'''function that inserts a new document in a collection'''


import pymongo


def insert_school(mongo_collection, **kwargs):
    '''insert_school function'''
    school = mongo_collection.insert_one(kwargs)
    return (school.inserted_id)
