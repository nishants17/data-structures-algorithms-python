class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() > level

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.parent == level:
            if self.children:
                for child in self.children:
                    child.print_tree()




        #p = self.parent



def build_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")
    newjersey = TreeNode("NJ")
    newjersey.add_child(TreeNode("Prince"))
    newjersey.add_child(TreeNode("Trent"))

    cali = TreeNode("Cali")
    cali.add_child(TreeNode("SJ"))
    cali.add_child(TreeNode("SF"))

    root.add_child(india)
    root.add_child(usa)
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(newjersey)
    usa.add_child(cali)

    root.print_tree(1)

if __name__ == '__main__':
    build_tree()