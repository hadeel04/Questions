# binary search tree

class binary_tree_node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def insert(root, key):
    if root is None:
        return binary_tree_node(key)

    if key < root.key:
        root.leftChild = insert(root.leftChild, key)
    elif key > root.key:
        root.rightChild = insert(root.rightChild, key)

    return root


def search(root, key):
    if root is None:
        return False

    elif root.key == key:
        return True

    elif root.key < key:
        return search(root.rightChild, key)

    else:
        return search(root.leftChild, key)


def delete(root, key):
    if root is None:
        return root

    if root.key > key:
        root.leftChild = delete(root.leftChild, key)
        return root
    elif root.key < key:
        root.rightChild = delete(root.rightChild, key)
        return root

    if root.leftChild is None:
        temp = root.rightChild
        del root
        return temp
    elif root.rightChild is None:
        temp = root.leftChild
        del root
        return temp

    else:

        succParent = root
        succ = root.rightChild
        while succ.leftChild is not None:
            succParent = succ
            succ = succ.leftChild

        if succParent != root:
            succParent.leftChild = succ.rightChild
        else:
            succParent.rightChild = succ.rightChild

        root.key = succ.key

        del succ
        return root


# ---------------------------------------------------------------
# the lowest common ancestor of two nodes in a binary tree.
def find_path(root, path, key):
    if root is None:
        return False

    path.append(root.key)

    if root.key == key:
        return True

    if ((root.leftChild is not None and find_path(root.leftChild, path, key)) or
            (root.rightChild is not None and find_path(root.rightChild, path, key))):
        return True

    path.pop()
    return False


def find_LCA(root, n1, n2):
    path1 = []
    path2 = []

    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


# ----------------------------------------------------------------------------
# the shortest path between two nodes in a graph.

def shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return start

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
            explored.append(node)

    return None


root = binary_tree_node(1)
root.leftChild = binary_tree_node(2)
root.rightChild = binary_tree_node(3)
root.leftChild.leftChild = binary_tree_node(4)
root.leftChild.rightChild = binary_tree_node(5)
root.rightChild.leftChild = binary_tree_node(6)
root.rightChild.rightChild = binary_tree_node(7)

print("LCA(4, 5) = %d" % (find_LCA(root, 4, 5, )))
print("LCA(4, 6) = %d" % (find_LCA(root, 4, 6)))
print("LCA(3, 4) = %d" % (find_LCA(root, 3, 4)))
