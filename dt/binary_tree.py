class BiinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add data in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BiinarySearchTreeNode(data) # leaf
        else:
            # add data in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BiinarySearchTreeNode(data) # leaaf
                

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        

        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # log(n)
    def search(self,val):
        if self.data == val:
            return True
        
        # val might be in the left subtree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
                
        # val migt be in the right subtree
        if val > self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BiinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__== "__main__":
    numbers = [17,4,1,20,9,23,18,34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20)) 
    print(numbers_tree.search(21))