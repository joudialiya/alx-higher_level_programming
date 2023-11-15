#!/usr/bin/pyhton3

class Board:
    def __init__(self, n):
        self.size = n
        self.current_line = 0:
        self.board = ""
        for i in range(0, n * n):
            self.borad += "."

    def children(self):
        for i in range(0, n):
            if self.board[i + self.current_line * self.size] == '.'
                new_board = str(self.board)
                new_board[i + self.current_line * self.size] == '#'
                #horizontal
                for row in range(0, self.size):
                    if new_board[row + self.current_line * self.size] == '.':
                        new_board[row + self.current_line * self.size] = '*'
                #vertical
                for line in range(0, self.size):
                    if new_board[i + line * self.size] == '.':
                        new_board[i + line * self.size] = '*':
                #left to rigth
                corr = lambda x: return ()
                for step in range(0, self.size):
                 
