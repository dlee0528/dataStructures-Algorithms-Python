class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    # count the number of parents
    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + " - " if self.parent else "" # tenary op
        print(prefix + self.data)

        if(len(self.children) > 0):
            for child in self.children: 
                child.print_tree()


def builid_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))


    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Nokia"))
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Samsung"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Lg"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = builid_product_tree()
    # print(root.get_level())
    root.print_tree()
    pass