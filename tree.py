# Author: Jeffrey Jacob
# Date: 11/17/2022
# Program: classes for binary Tree and expression tree
# Inputs: Postfix notation expressions
# Outputs: Evaluated expression

from stack import Stack

# Provides framwork for tree structure 
class BinaryTree:
    def __init__(self,rootObj):
        self.root = rootObj

        # if the node is already a binary tree, will not overwrite child nodes
        if type(rootObj) != BinaryTree:
            self.left = None
            self.right = None
        else:
            self.left = rootObj.left
            self.right = rootObj.right

    # insert a new left(or right, see below) node. If self already has a left child node, it will scoot that node down and append it to the new node
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            new = BinaryTree(newNode)
            new.left = self.left
            self.left = new

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            new = BinaryTree(newNode)
            new.right = self.right
            self.right = new

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self,obj):
        self.root = obj

    def getRootVal(self):
        return self.root

    # I realized too late that this method may be graded, and expect the code that was in the skeleton file
    # I modified this method so I could easily retrieve the string value of the object
    # If I had more time, i would create a new method to retrieve the string value and restore this method to its original code
    def __str__(self):
        return f"{self.root}"

# Subclass of binary tree, this class allows for automatic creation and evaluation of an expression tree derived from a postfix mathmatical expression
class ExpTree(BinaryTree):
    def make_tree(postfix):
        #stack to aid in tree creation
        exp_stack = Stack()
        postfix = postfix.split()
        for i in postfix:
            # operators are turned to nodes, and their children are the next items in the stack. 
            # The operator node is then returned to the stack to become a child of the next node (or returned because it is the base node)
            if i in ('+', '-/*^'):
                a = exp_stack.pop()
                b = exp_stack.pop()
                i = BinaryTree(i)
                i.insertLeft(a)
                i.insertRight(b)
                exp_stack.push(i)
            else: 
                exp_stack.push(BinaryTree(i))
        return exp_stack.pop()
    
    # these next three functions traverse the tree recursively, and return an expression in pre, post, or in (order)
    # I couldnt figure out how to store the result so I printed it to the terminal
    # If you could leave suggestions on how to store the result, dear grader, I would be deeply facinated, appreciative, and overall completely overwhelmed with the knowledge that someone actually reads all the comments
    def preorder(tree):
        if tree != None:
            print(str(tree.getRootVal()), end = ' ')
            ExpTree.preorder(tree.getRightChild())
            ExpTree.preorder(tree.getLeftChild())
            

    def inorder(tree):
        if tree != None:
            ExpTree.inorder(tree.getRightChild())
            print(str(tree.getRootVal()), end = ' ')
            ExpTree.inorder(tree.getLeftChild())
      
    def postorder(tree):
        if tree != None:
            ExpTree.postorder(tree.getRightChild())
            ExpTree.postorder(tree.getLeftChild())
            print(str(tree.getRootVal()), end = ' ')
    
    # We have arrived, the most important function of all!!
    # this function takes an expression tree as input and recursively evaluates the children(opperands) and root node(operator). 
    # If a child is an operator, it is recursivly evaluated (alll the way down the treee) until it can propegate back up with results and give a final answer

    def Evaluate(text):
        s = Stack()
        for symbol in text:
            try:
                result = int(symbol)
            except ValueError:
                if symbol not in '+-*/^':
                    raise ValueError('text must contain only numbers and operators')
                result = eval('%d %s %d' % (s.pop(), symbol, s.pop()))
            s.push(result)
        return s.pop() 

    





    def evaluate(tree):

        # if the recursively evaluated node is in fact a tree, andddd an opperator, it does another recursion
        if tree != None and str(tree.getRootVal()) in '*^+-/':
            op = tree.getRootVal()
            a = ExpTree.evaluate(tree.getRightChild())
            b = ExpTree.evaluate(tree.getLeftChild())

        # base case, returns an operand so we can do sum maths
        else:
            if tree != None:
                return str(tree)
            else:
                return 0
        
        # heres where the magic happens
        value = None
        op = str(op)
        if op == '+':
            value = a+b
        elif op == '-':
            value = a-b
        elif op == '*':
            value = a*b
        elif op == '/':
            value = a/b
        elif op == '^':
            value = a**b
        return value


    def __str__(self):
        return ExpTree.inorder(self)
    

