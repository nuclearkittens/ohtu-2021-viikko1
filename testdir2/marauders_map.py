import random
from time import sleep

class MaraudersMap:
    def __init__(self, height=20, width=20):
        self._map = []
        self._height = height
        self._width = width

    def _new_map(self):
        # TODO: random maps woop woop
        pass

    def insult(self):
        # quotes are from Harry Potter and the Prizoner of Azkaban,
        # 2004 UK paperback ed., p. 311
        insults = [
            '''Mr Moony presents his compliments to Professor Snape,
            and begs him to keep his abnormally large nose out of other people's business.''',
            '''Mr Prongs agrees with Mr Moony, and would like to add that
            Professor Snape is an ugly git.''',
            '''Mr Padfoot would like to register his astonishment that an idiot like
            that ever became a Professor.''',
            '''Mr Wormtail bids Professor Snape good day, and advises
            him to wash his hair, the slimeball.'''
        ]

        for i in insults:
            print(i)
            sleep(5)

