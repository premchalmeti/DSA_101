from ds.trees.tree import (
    Tree as GeneralizedTree, 
    Node as GeneralizedNode
)


class TrieNode(GeneralizedNode):
    def __init__(self, data):
        super().__init__(data)
        self.wrd_cnt = 0
        self.childs = {}

    def append_child(self, w, n):
        self.childs[w] = n

    def get_child(self, w):
        if isinstance(w, TrieNode):
            w = w.get_data()
        return self.childs.get(w)


class TrieTree(GeneralizedTree):
    def __init__(self):
        root = TrieNode('root')
        super().__init__(n=root)

    def insert_word(self, wrd):
        cur = self.get_root()

        for w in wrd:
            p = cur.get_child(w)

            if not p:
                nn = TrieNode(w)
                cur.append_child(w, nn)
                cur = nn
            else:
                cur = p

        cur.wrd_cnt += 1

    def suggest_rec(self, node, query, suggestions):
        if node.wrd_cnt > 0:
            suggestions.extend([query] * node.wrd_cnt)

        for w, n in node.childs.items():
            self.suggest_rec(n, query+w, suggestions)
        return suggestions

    def suggest(self, query):
        c = self.get_root()
        prefix = ""

        for w in query:
            c = c.get_child(w)
            if not c:
                return []
            prefix += w

        return self.suggest_rec(c, prefix, [])

    def delete(self, wrd):
        pass

    def update(self, wrd):
        self.delete(wrd)
        self.insert_word(wrd)

    def search(self, wrd):
        cur = self.get_root()

        for w in wrd:
            p = cur.get_child(w)
            if not p:
                return False
            cur = p

        return True and cur.wrd_cnt > 0


if __name__ == '__main__':
    repository = ['pqrs', 'pqss', 'pqst', 'pqss']
    query = 'pqss'
    t = TrieTree()
    list(map(t.insert_word, repository))
    print(f"Searching '{query}' in {repository} = ", t.search(query))
