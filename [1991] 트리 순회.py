import sys

n = int(sys.stdin.readline())
tree = dict()
root = 'A'

class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def preorder(node):
    sys.stdout.write(node.data)
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])

def inorder(node):
    if node.left:
        inorder(tree[node.left])
    sys.stdout.write(node.data)
    if node.right:
        inorder(tree[node.right])

def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    sys.stdout.write(node.data)

for i in range(n):
    a, b, c = sys.stdin.readline().split()
    if a == root:
        tree[root] = Node()
        tree[root].data = a
        if b != '.':
            tree[root].left = b
            tree[b] = Node()
            tree[b].data = b
        if c != '.':
            tree[root].right = c
            tree[c] = Node()
            tree[c].data = c
    else:
        if b != '.':
            tree[a].left = b
            tree[b] = Node()
            tree[b].data = b
        if c != '.':
            tree[a].right = c
            tree[c] = Node()
            tree[c].data = c

preorder(tree[root])
sys.stdout.write('\n')
inorder(tree[root])
sys.stdout.write('\n')
postorder(tree[root])
