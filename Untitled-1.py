import graphviz

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def tree_to_graphviz(node, dot=None):
    if dot is None:
        dot = graphviz.Digraph()
    dot.node(str(id(node)), str(node.data))
    for child in node.children:
        dot.edge(str(id(node)), str(id(child)))
        tree_to_graphviz(child, dot)
    return dot

def main():
    # Create the tree structure
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")
    grandchild1 = TreeNode("Grandchild 1")
    grandchild2 = TreeNode("Grandchild 2")
    grandchild3 = TreeNode("Grandchild 3")

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    child1.add_child(grandchild1)
    child2.add_child(grandchild2)
    child2.add_child(grandchild3)

    # Convert tree to Graphviz representation
    dot = tree_to_graphviz(root)

    # Render and display the graph
    dot.render('tree_graph', format='png', cleanup=True)

if __name__ == "__main__":
    main()
