import random as randy
import os
from .read import read_file


def load_sets(sets_file):
    set_list = read_file(sets_file)
    results = {}

    # Skip the first line of each file, it's the header
    for item in set_list[1:]:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sets_file)), item[1])
        results[item[1].replace('.csv', '')] = {
            'lines': read_file(file_path)[1:],
            'name': item[0]
        }

    return results


class Quotes(object):
    # Relative path to this __init__ file
    SETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/index.csv")

    def __init__(self, sets_file=SETS):
        self.sets_file = sets_file
        self.quotes = load_sets(self.sets_file)

    def random(self, keys=None):
        # Take only a few sets into account
        if isinstance(keys, list):
            _quotes = {key: self.quotes[key] for key in keys if key in self.quotes}

        # Take all sets into account
        else:
            _quotes = self.quotes

        if len(_quotes) > 0:
            key = randy.choice(list(_quotes.keys()))
            return key, randy.choice(_quotes[key]['lines'])[0]
        else:
            return None

    def persons(self):
        return list(self.quotes.keys())

    def sets(self):
        # return {k: v['key'] for k, v in self.quotes.items()}
        return [k for k, v in self.quotes.items()]

    def get_set(self, key):
        """
        Get 1 specific set of quotes based on a key. The key of a set is the name of the csv file,
        with or without extension.

        :param key: a string with key of the set
        :return: a list of quotes
        """
        assert key

        if key in self.quotes:
            return self.quotes[key]['lines']

        raise KeyError(key)
