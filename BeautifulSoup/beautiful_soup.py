from random import random

"""
inspired by https://robertheaton.com/2018/07/20/project-2-game-of-life/index.html
"""

class BeautifulSoup():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_state(self, fraction = 0.5):
        self.random_state = [[1 for x in range(self.width) if random() > fraction else 0] for y in range(self.height)]

        return self.random_state