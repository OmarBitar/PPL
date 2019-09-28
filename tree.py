# CS3210 - Principles of Programming Languages - Fall 2019
# A tree data-structure
# Author: Thyago tmota
# Date: 09/09/19

TAB = "   "

class Tree:

    def __init__(self):
        self.data = None
        self.children = []

    def add(self, child):
        self.children.append(child)

    def print(self, tab = ""):
        if self.data != None:
            print(tab + self.data)
            tab += TAB
            for child in self.children:
                if isinstance(child, Tree):
                    child.print(tab)
                else:
                    print(tab + child)
