from stack import Stack
from tree import *
def infix_to_postfix(expression):
    op_stack = Stack()
    tokens = []
    for i in expression:
        if i != ' ':
            tokens.append(i)
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    result = []
    final_result = ''
    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            result.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            popped = ''
            while popped != '(':
                result.append(popped)
                popped = op_stack.pop()
        else:
            while not op_stack.isEmpty() and prec[op_stack.peek()] >= prec[token]:
                result.append(op_stack.pop())
            else:
                op_stack.push(token)
    while not op_stack.isEmpty():
        result.append(op_stack.pop())
    for i in result:
        final_result += i 
    return final_result

def calculate(expression):
    postfix = infix_to_postfix(expression)
    tree = ExpTree.make_tree(postfix)
    ans = ExpTree.evaluate(tree)
    ans = ExpTree.Evaluate(str(tree))
    print(ans)
    
    
    




    
    # only positive floats and ints
    # only +-/*^

    # implementation
    # infix to postfix on the expression
    # make expression tree
    # evaluate with the binary tree
    # returns answer as float




while True:
    a = input("expression")
    calculate(a)
