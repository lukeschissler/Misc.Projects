from random import random
from time import sleep

"""
inspired by https://robertheaton.com/2018/07/20/project-2-game-of-life/index.html
"""

class SoupError(Exception):

    def __init__(self, msg):
        self.message = msg

class BeautifulSoup():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def resume_state(self, file_name):
        with open(file_name) as f:
            my_lines = f.readlines()

        file_state = [list(map(lambda x : int(x), x.strip())) for x in my_lines]
        self.height = len(file_state)
        self.width = len(file_state[0])

        return file_state

    def set_random_state(self, fraction = 0.5) -> list:
        if fraction < 0 or fraction > 1:
            raise SoupError('Invalid fraction entered.')

        random_state = [[1 if random() < fraction else 0 for x in range(self.width)] for y in range(self.height)]

        return random_state

    def render(self, state) -> None:
        print('-'*(self.width+2))
        for x in state:
            outs = '|'
            for y in x:
                if y:
                    outs += '#'
                else:
                    outs += ' '
            outs += '|'
            print(outs)
        print('-'*(self.width+2))

        return None

    def iterate(self, prev_state) -> list:
        new_state = [[0 for x in range(self.width)] for y in range(self.height)]
        neighbors = [(1,-1), (1,0), (1,1), (0, -1), (0,1), (-1, -1), (-1,0), (-1,1)]

        for row in range(self.height):
            for column in range(self.width):
                neighbor_sum = 0
                for n in neighbors:
                    if row+n[0] < 0 or column+n[1] < 0:
                        pass
                    else:
                        try:
                            neighbor_sum += prev_state[row+n[0]][column+n[1]]
                        except:
                            pass

                if not prev_state[row][column]:
                    if neighbor_sum == 3:
                        new_state[row][column] = 1
                elif neighbor_sum == 2 or neighbor_sum == 3:
                    new_state[row][column] = 1
                else:
                    new_state[row][column] = 0
        return new_state

    def run(self, state):
        self.render(state)
        while True:
            sleep(1)
            state = self.iterate(state)
            self.render(state)


def main():

    my_soup = BeautifulSoup(800,200)
    my_rand_state = my_soup.set_random_state(.5)
    my_soup.render(my_rand_state)
    my_next_state = my_soup.iterate(my_rand_state)
    my_soup.render(my_next_state)
    my_soup.run(my_rand_state)

if __name__ == '__main__':
    main()