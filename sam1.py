class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_auto_completions(self, prefix):
        prefix_node = self.search(prefix)
        if prefix_node:
            suggestions = []
            self.dfs(prefix_node, prefix, suggestions)
            return suggestions
        else:
            return []

    def dfs(self, node, prefix, suggestions):
        if node.is_word:
            suggestions.append(prefix)
        for char, child in node.children.items():
            self.dfs(child, prefix + char, suggestions)


# Read the input
N = int(input())
dictionary = Trie()
for _ in range(N):
    word = input()
    dictionary.insert(word)

Q = int(input())
for _ in range(Q):
    query = input()
    suggestions = dictionary.get_auto_completions(query)
    if suggestions:
        suggestions.sort()
        for word in suggestions:
            print(word)
    else:
        dictionary.insert(query)
        print("No suggestions")
