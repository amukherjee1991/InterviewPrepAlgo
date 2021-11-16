class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    # laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    laptop.add_child(TreeNode("MS"))




    apple = TreeNode("Mac")
    apple.add_child(TreeNode("Macbook"))
    apple.add_child(TreeNode("Macbook Pro"))
    apple.add_child(TreeNode("Macbook Air"))

    # laptop2.add_child(TreeNode("MS"))

    # laptop.addChild()


    tablet=TreeNode("Tablet")
    tablet.add_child(TreeNode("ipad"))
    tablet.add_child(TreeNode("galaxy Tab"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))


    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    
    smartwatch=TreeNode("Smartwatch")
    smartwatch.add_child(TreeNode("apple"))
    smartwatch.add_child(TreeNode("samsung"))
    smartwatch.add_child(TreeNode("garmin"))

    # applewatch=smartwatch.add_child(TreeNode("Apple watch6"))
    # smartwatch.apple.add_child(TreeNode("something"))

    # Tree('C111')

    # child111 = Tree('C111')

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.add_child(tablet)
    root.add_child(smartwatch)
    laptop.add_child(apple)

    # laptop.addChild()

    # root.smartwatch.add_child()





    # cellphone.add_child(Ios)
    
    root.print_tree()

if __name__ == '__main__':
    build_product_tree()