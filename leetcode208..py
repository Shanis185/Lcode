class Trie(object):

    def __init__(self):
        self.trie={}

    def insert(self, word):
        d=self.trie
        for i in word:
            if i not in d:
                d[i]={}
            d=d[i]
        d['.']='.'
        

    def search(self, word):
        d=self.trie
        for i in word:
            if i not in d:
                return False
            d=d[i]
        return '.' in d

        

    def startsWith(self, prefix):
        d=self.trie
        for i in prefix:
            if i not in d:
                return False
            d=d[i]

        return True