#!/usr/bin/env python3
'''Function that takes two integer arguments'''


def index_range(page, page_size):
    '''index_range function'''
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return start_index, end_index
