"""
Inspired by https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/index.html
"""

class TTTException(Exception):

    def __init__(self, msg):
        self.message = msg

class TicTacToe:

    def __init__(self):
        self.board = [['_', '_', '_'] for x in range(3)]
        self.win_states = [{'X'}, {'O'}]

    def render(self) -> None:
        print('-'*7)
        for line in self.board:
            print('|'+' '.join(line)+'|')
        print('-'*7)

        return None

    def to_coor(self, index):
        return (index // 3, index % 3)

    def player_move(self, player) -> None:
        status = True
        while status:
            move = int(input('Enter a spot to move (1-9) for an unoccupied spot: '))

            if type(move) != int:
                print('Enter a number.')
            elif move < 0 or move > 9:
                print('Enter a number between 1-9.')
            else:
                x_pos, y_pos = self.to_coor(move-1)
                if self.board[x_pos][y_pos] != '_':
                    print('Enter a position for an unoccupied spot.')
                else:
                    self.board[x_pos][y_pos] = player
                    status = False

        return None

    def check_diagonals(self) -> bool:
        r_diag, l_diag = [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
        r_diags, l_diags = set([self.board[x][y] for x, y in r_diag]), set([self.board[x][y] for x, y in l_diag])

        return r_diags in self.win_states or l_diags in self.win_states

    def check_rows(self) -> bool:
        t_rows, m_rows, b_rows = set(self.board[0]), set(self.board[1]), set(self.board[2])

        return t_rows in self.win_states or b_rows in self.win_states or m_rows in self.win_states

    def check_columns(self) -> bool:
        l_col, m_col, r_col = [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2),(1,2),(2,2)]
        l_cols, m_cols, r_cols = set([self.board[x][y] for x, y in l_col]), set([self.board[x][y] for x, y in m_col]), \
                                    set([self.board[x][y] for x, y in r_col])

        return l_cols in self.win_states or r_cols in self.win_states or m_cols in self.win_states

    def check_draw(self) -> bool:
        return '_' not in ''.join([''.join(x) for x in self.board])

    def check_state(self) -> bool:
        return self.check_diagonals() or self.check_rows() or self.check_columns()

    def play(self) -> None:
        players = ['O', 'X']
        for i in range(9):
            self.render()
            self.player_move(players[i%2])

            if self.check_state():
                self.render()
                print(f'{players[i%2]}\'s player wins!')
                return None

        self.render()
        print('The result is a draw.')
        return None

def main():
    my_board = TicTacToe()
    my_board.play()

if __name__ == '__main__':
    main()