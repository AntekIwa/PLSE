class tree_node:
    def __init__(self, is_word):
        self.is_word = is_word
        self.adj = dict()

class DAWG:
    def __init__(self, words):
        self.root = tree_node(False)
        for word in words:
            node = self.root #we are starting on the begining of the graph
            for letter in word:
                if letter not in node.adj.keys(): #we dont have this edge
                    node.adj[letter] = tree_node(False)
                node = node.adj[letter] #we are moving to next letter/node
            node.is_word = True #we are processing word so in this node we know that we have a correct word

    def find_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node.adj.keys(): #we dont have this word
                return None
            node = node.adj[letter]
        return node

    def is_word(self, word):
        node = self.find_word(word)
        if node is None: #we dont have this word in dictionary
            return False
        return node.is_word


def sjp():
    with open('slowa.txt', 'rt') as file:
        words = []
        for line in file:
            word = line.strip()
            words.append(word)
    print("slowa wczytane, liczba slow: ", len(words))
    return DAWG(words)
# print("start")
# sjp()
# print("gotowe")

