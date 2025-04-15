# === Estruturas de Dados: BST e AVL ===
import pandas as pd
import time
import random
import sys
sys.setrecursionlimit(50000)  # ou mais, se necessário

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            return Node(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

class AVLNode(Node):
    def __init__(self, key, data):
        super().__init__(key, data)
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if not node:
            return AVLNode(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def height(self):
        return self._get_height(self.root)

# === Leitura e pré-processamento do CSV ===

df = pd.read_csv("dados_abertos_ogu_2024122.csv", sep=';', encoding='utf-8')
df = df.dropna(subset=['cod_operacao'])
df = df.drop_duplicates(subset=['cod_operacao'])
df['cod_operacao'] = df['cod_operacao'].astype(str)

# === Criação das árvores ===

bst = BST()
avl = AVLTree()

# Inserção na BST
start_bst = time.time()
for _, row in df.iterrows():
    bst.insert(row['cod_operacao'], row.to_dict())
end_bst = time.time()

# Inserção na AVL
start_avl = time.time()
for _, row in df.iterrows():
    avl.insert(row['cod_operacao'], row.to_dict())
end_avl = time.time()

# Alturas
altura_bst = bst.height()
altura_avl = avl.height()

# Busca por 100 elementos aleatórios
amostras = random.sample(list(df['cod_operacao']), 1000)

start_search_bst = time.time()
for cod in amostras:
    bst.search(cod)
end_search_bst = time.time()

start_search_avl = time.time()
for cod in amostras:
    avl.search(cod)
end_search_avl = time.time()

# Função de contagem de nós
def contar_nos(node):
    if node is None:
        return 0
    return 1 + contar_nos(node.left) + contar_nos(node.right)

# Contagem de elementos
total_entrada = df['cod_operacao'].nunique()
total_bst = contar_nos(bst.root)
total_avl = contar_nos(avl.root)

# === Exibir Resultados ===

print("\n--- RESULTADOS ---")
print(f"Total de elementos únicos no CSV: {total_entrada}")
print(f"Total de nós inseridos na BST: {total_bst}")
print(f"Total de nós inseridos na AVL: {total_avl}")
print(f"\nTempo de inserção BST: {end_bst - start_bst:.6f} segundos")
print(f"Tempo de inserção AVL: {end_avl - start_avl:.6f} segundos")
print(f"Tempo de busca BST (100 elementos): {end_search_bst - start_search_bst:.6f} segundos")
print(f"Tempo de busca AVL (100 elementos): {end_search_avl - start_search_avl:.6f} segundos")
print(f"Altura da BST: {altura_bst}")
print(f"Altura da AVL: {altura_avl}")
