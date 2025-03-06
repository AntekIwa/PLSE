class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(None)
            self.tiles.append(row)

    def __str__(self):
        return '\n'.join(''.join(x if x is not None else '_' for x in row) for row in self.tiles)

    def all_position(self):
        pos = []
        for r in range(self.size):
            for c in range(self.size):
                pos.append((r,c))
        return pos

    def get_tile(self, pos):
        row, col = pos
        return self.tiles[row][col]

    def set_tile(self, pos, tile):
        row, col = pos
        self.tiles[row][col] = tile

    def in_bounds(self, pos):
        row, col = pos
        return 0 <= row < self.size and 0 <= col < self.size

    def is_empty(self, pos):
        row, col = pos
        return self.in_bounds(pos) and self.get_tile(pos) is None

    def is_filled(self, pos):
        row, col = pos
        return self.in_bounds(pos) and self.get_tile(pos) is not None

    def copy(self):
        res = Board(self.size)
        for pos in self.all_position():
            res.set_tile(pos, self.get_tile(pos))
        return res


def sample_board():
    result = Board(7)
    result.set_tile((1,1), "d")
    result.set_tile((2,1), "o")
    result.set_tile((3,1), 'm')
    result.set_tile((1, 3), "m")
    result.set_tile((2, 3), "e")
    result.set_tile((3, 3), 't')
    return result

