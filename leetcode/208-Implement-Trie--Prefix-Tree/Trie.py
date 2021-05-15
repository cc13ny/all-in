class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = ''
        self.isWord = False  # same to a random number for a complete word
        self.children = {}  # {c : TrieNode}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        children = self.root.children
        for c in word:
            if c not in children:
                tmp = TrieNode()
                tmp.c = c
                children[c] = tmp
            treenode = children[c]
            children = treenode.children
        treenode.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        children = self.root.children
        for c in word:
            if c not in children:
                return False
            treenode = children[c]
            children = treenode.children
        return treenode.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        children = self.root.children
        for c in prefix:
            if c not in children:
                return False
            treenode = children[c]
            children = treenode.children
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
