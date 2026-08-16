class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d['/'] = '/'
        

    def search(self, word: str) -> bool:
        def search_in_dict(word, d):
            for i, c in enumerate(word):
                if c not in d:
                    if c == '.':
                        for char in d:
                            if char != '/' and search_in_dict(word[i+1:], d[char]):
                                return True
                    return False
                else:
                    d = d[c]
            return '/' in d
        return search_in_dict(word, self.trie)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)