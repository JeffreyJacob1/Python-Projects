# author: Jeffrey Jacob
# script: codecs
# inputs: binary string or ASCII message
# outputs: decoded binary, encoded binary

import numpy as np

#base class, converts binary to text and vis versa
class Codec():
    def __init__(self):
        self.name = 'binary'
        self.delimiter = '00100011' # a hash symbol '#' 

    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.delimiter:
                break 
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))       
        return text 

class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = '#'  # you may need to set up it to a corresponding binary code
        self.shift = shift    
        self.chars = 256      # total number of characters

    # convert text into binary form
    def encode(self, text):
        data = ''
        if type(text) == str:
            for i in text:
                code = (ord(i) + self.shift) % self.chars
                data += format(code, "08b")
        else:
            print('Format error')
        return data
    
    # convert binary data into text
    def decode(self, data):
        text = ''    
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            letter = chr(int(byte,2))  
            shifted = ord(letter) - self.shift
            letter = chr(shifted)
            if letter == self.delimiter:
                break
            text += letter
        return text 
        

# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
        
class HuffmanCodes(Codec):
    
    def __init__(self):
        self.nodes = None
        self.name = 'huffman'
        self.key = {}
        self.decoded = ''
        self.delimiter = '#'

    # make a Huffman Tree    
    def make_tree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))
            
        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)

            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]

            # assign codes
            left.code = '0'
            right.code = '1'

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
            
        return nodes

    # traverse a Huffman tree, saves a dictionary where keys are the encoded letters and values are the binary representation
    def traverse_tree(self, node, val=''):
        next_val = val + node.code
        if(node.left):
            self.traverse_tree(node.left, next_val)
        if(node.right):
            self.traverse_tree(node.right, next_val)
        if(not node.left and not node.right):
            self.key[node.symbol] = next_val
            return node.symbol


    # convert text into binary form
    def encode(self, text):
        binary = ''
        data = {}
        for char in text:
            if char in data.keys():
                data[char] += 1
            else:
                data[char] = 1   
        self.nodes = self.make_tree(data)
        self.traverse_tree(self.nodes[0])
        for char in text:
            binary += self.key[char]
        return binary

    # a helper function for huffman decode
    # takes val as an input, than navigates the huffman tree based on val
    # returns the leaf node reached by navigating the huffman tree
    def find_node(self, node, val = ' '):
        val = val
        if node != None:
            if val == '':
                self.decoded = node.symbol
            elif val[0] == '0':
                val = val[1:]
                self.find_node(node.left, val)
            elif val[0] == '1':
                val = val[1:]
                self.find_node(node.right, val)
        return self.decoded

        
     
    # convert binary data into text
    def decode(self, data):
        text = ''
        self.key = {}
        found_message = False
        check = ''
        while not found_message: 
            # continually adds data to 'check' and checks if it returns a letter. if a letter is returned, 'check' is cleared and the letter is added to the message
            if len(data) >=1:
                check += data[0]
                data = data[1:]
            if len(self.find_node(self.nodes[0], check)) == 1:
                result = self.find_node(self.nodes[0], check)
                if result == self.delimiter:
                    found_message = True
                    continue
                else:
                    text += result
                check = ''
        return text

# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text)
    print('Binary:',binary)
    data = c.decode(binary)
    print('Text:',data)

    cc = CaesarCypher()
    binary = cc.encode(text)
    print('Binary:',binary)
    data = cc.decode(binary)
    print('Text:',data)

    h = HuffmanCodes()
    binary = h.encode(text)
    print('Binary:',binary)
    data = h.decode(binary)
    print('Text:',data)  

