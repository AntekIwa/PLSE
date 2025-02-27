from dawg_generator import sjp
from board import sample_board

class State:
    def __init__(self, dict, board, rack):
        self.dict = dict
        self.rack = rack
        self.board = board
    def found_word(self, word):
        print("we found new word: ", word)
        board_if_we_play = self.board.copy()

    def up(self, pos):
        row, col = pos
        return row - 1, col

    def down(self, pos):
        row, col = pos
        return row + 1, col

    def left(self, pos):
        row, col = pos
        return row, col - 1

    def right(self, pos):
        row, col = pos
        return row, col + 1

    def find_good(self):
        res = []
        for pos in self.board.all_position():
            empty = self.board.is_empty(pos)
            is_adj = self.board.is_filled(self.left(pos)) or self.board.is_filled(self.right(pos)) or self.board.is_filled(self.up(pos)) or self.board.is_filled(self.down(pos))
            if empty and is_adj:
                res.append(pos)
        return res

    def generate(self, actual_word, node):
        if node.is_word:
            self.found_word(actual_word)
        for letter in node.adj.keys():
            if letter in self.rack:
                self.rack.remove(letter)
                self.generate(actual_word + letter, node.adj[letter])
                self.rack.append(letter)
    def find_all_words(self):
        anchors = self.find_good()
        for pos in anchors:
            if self.board.is_filled(self.board.left(pos)):
                word = ""
                tmp_pos = self.board.left(pos)
                while(self.board.is_filled(tmp_pos)):
                    word = self.board.get_tile(tmp_pos) + word
                    tmp_pos = self.board.left(tmp_pos)
                node = self.dawg.find_word(word) #lets find word on the left side of our tile
                if node is not None:
                    self.generate(word, node)


        self.generate("", self.dict.root)


solver = State(sjp(), sample_board(), ["b", "l", "m","o","a"])
print(solver.board)
print("szukamy...")

solver.find_all_words()

