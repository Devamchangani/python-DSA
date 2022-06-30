class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def build_product_tree():
        root = TreeNode('Electronics')

        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Thinkpad"))
        laptop.add_child(TreeNode("Surface"))


        CellPhone = TreeNode("Cell phone")
        CellPhone.add_child(TreeNode("i Phone"))
        CellPhone.add_child(TreeNode("Realme"))
        CellPhone.add_child(TreeNode("Samsung"))

        TV = TreeNode("TV")
        TV.add_child(TreeNode("LG"))
        TV.add_child(TreeNode("Samsung"))


        root.add_child(laptop)
        root.add_child(CellPhone)
        root.add_child(TV)

        root.print_tree()

if __name__ == '__main__':
    pass