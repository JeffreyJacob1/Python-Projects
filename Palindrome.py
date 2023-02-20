from  stack import Stack
def evaluatePostfix(exp):
         
        # Iterate over the expression for conversion
        for i in exp:
             
            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)
 
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
 
        return int(self.pop())


    
b = '32-'
string = str(b)
a = evaluatePostfix(string)
print(a)
