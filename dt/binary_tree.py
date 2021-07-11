class BiinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exists
        
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
    
    def delete(self, val):
        # find in the left substree
        if val < self.data:
            if self.left: # if there's any left subtree
                self.left = self.left.delete(val) # recursively call delete
    
        # find in the right subtree
        elif val > self.data:
            if self.right: # if there's any right subtree
                self.right = self.right.delete(val) # recursively call delete
        
        else:
            if self.left is None and self.right is None: # reach the laast node point
                return None

            elif self.left is None:
                return self.right

            elif self.right is None:
                return self.left


            min_val = self.right.find_min()
            self.data = min_val # make a copy
            self.right = self.right.delete(min_val)

        return self

    
    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()


def build_tree(elements):
    root = BiinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__== "__main__":
    # numbers = [17,4,1,20,9,23,18,34, 18, 4]
    # numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(20)) 
    # print(numbers_tree.search(21))

    # delete
    numbers_tree = build_tree([17,4,1,20,9,23,18,34])
    numbers_tree.delete(20)
    print("After deleting 20", numbers_tree.in_order_traversal())