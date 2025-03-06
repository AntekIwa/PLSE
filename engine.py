from dawg_generator import sjp
from board import sample_board

class State:
    def __init__(self, dict, board, rack):
        self.dict = dict
        self.rack = rack
        self.board = board
        self.cross_check_result = None
        self.direction = None

    def found_word(self, word, last_pos):
        print("we found new word: ", word)
        board_if_we_play = self.board.copy()
        play_pos = last_pos
        word_idx = len(word) - 1
        while(word_idx >= 0):
            board_if_we_play.set_tile(play_pos, word[word_idx])
            play_pos = self.left(play_pos)
            word_idx -= 1
        print(board_if_we_play)
        print()

    def cross_check(self):
        result = dict()
        for pos in self.board.all_position():
            if self.board.is_filled(pos):
                continue
            letters_up = ""
            scan_pos = pos
            while self.board.is_filled(self.up(scan_pos)):
                scan_pos = self.up(scan_pos)
                letters_up = self.board.get_tile(scan_pos) + letters_up

            letters_down = ""
            scan_pos = pos
            while self.board.is_filled(self.down(scan_pos)):
                scan_pos = self.down(scan_pos)
                letters_down =  letters_down + self.board.get_tile(scan_pos)
            if len(letters_up) == 0 and len(letters_down) == 0:
                legal_here = list('aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż')
            else:
                legal_here = []
                for letter in 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż':
                    word_formed = letters_up + letter + letters_down
                    if self.dict.is_word(word_formed):
                        legal_here.append(letter)
            result[pos] = legal_here
        return result

    def left(self, pos):
        row, col = pos
        if self.direction == 'across':
            return row, col - 1
        else:
            return row - 1, col

    def right(self, pos):
        row, col = pos
        if self.direction == 'across':
            return row, col + 1
        else:
            return row + 1, col

    def up(self, pos):
        row, col = pos
        if self.direction == 'across':
            return row - 1, col
        else:
            return row, col - 1

    def down(self, pos):
        row, col = pos
        if self.direction == 'across':
            return row + 1, col
        else:
            return row, col + 1

    def find_good(self):
        res = []
        for pos in self.board.all_position():
            empty = self.board.is_empty(pos)
            is_adj = self.board.is_filled(self.left(pos)) or self.board.is_filled(self.right(pos)) or self.board.is_filled(self.up(pos)) or self.board.is_filled(self.down(pos))
            if empty and is_adj:
                res.append(pos)
        return res

    def left_part(self, actual_word, node, pos, limit):
        self.extend_right(actual_word, node, pos)
        if limit > 0:
            for letter in node.adj.keys():
                if letter in self.rack:
                    self.rack.remove(letter)
                    self.left_part(actual_word + letter, node.adj[letter],pos, limit - 1)
                    self.rack.append(letter)

    def extend_right(self, actual_word, node, next_pos):
        if node.is_word and  (self.board.in_bounds(next_pos) == False or self.board.is_empty(next_pos)):
            self.found_word(actual_word, self.left(next_pos))
        if self.board.in_bounds(next_pos):
            if self.board.is_empty(next_pos):
                for letter in node.adj.keys():
                    if letter in self.rack and letter in self.cross_check_result[next_pos]:
                        self.rack.remove(letter)
                        self.extend_right(actual_word + letter, node.adj[letter], self.right(next_pos))
                        self.rack.append(letter)
            else:
                on_board = self.board.get_tile(next_pos)
                if on_board in node.adj.keys():
                    self.extend_right(actual_word + on_board, node.adj[on_board], self.right(next_pos))


    def find_all_words(self):
        for direct in ['across', 'down']:
            self.direction = direct
            anchors = self.find_good()
            self.cross_check_result = self.cross_check()
            for pos in anchors:
                if self.board.is_filled(self.left(pos)):
                    word = ""
                    tmp_pos = self.left(pos)
                    while(self.board.is_filled(tmp_pos)):
                        word = self.board.get_tile(tmp_pos) + word
                        tmp_pos = self.left(tmp_pos)
                    node = self.dict.find_word(word) #lets find word on the left side of our tile
                    if node is not None:
                        self.extend_right(word, node, pos)
                else:
                    limit = 0
                    scan_pos = pos
                    while self.board.in_bounds(self.left(scan_pos)) and self.left(scan_pos) not in anchors:
                        limit += 1
                        scan_pos = self.left(scan_pos)
                    self.left_part("", self.dict.root, pos, limit)



solver = State(sjp(), sample_board(), ["m", "a", "a"])
print(solver.board)
print("szukamy...")
print(solver.dict.is_word("domy"))
solver.find_all_words()

