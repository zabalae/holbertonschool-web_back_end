#!/usr/bin/env python3
'''Simple pagination'''

import csv
from typing import List


def index_range(page, page_size):
    '''index_range function'''
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get_page function'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        init, end = index_range(page, page_size)

        return self.dataset()[init:end]
