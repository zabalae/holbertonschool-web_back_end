#!/usr/bin/env python3
'''function that retunrs the list of school having a specific topic'''


def schools_by_topic(mongo_collection, topic):
    '''schools_by_topic function'''
    return [x for x in mongo_collection.find({'topics': topic})]
