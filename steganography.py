# author: Jeffrey Jacob
# script: steganography
# inputs: string and image OR encoded image
# outputs: encoded image OR string

#libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    # converts message to binary string using codecs
    # encodes binary string in specified image file
    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message + self.delimiter
            self.binary = binary
            
            message = [x for x in self.binary]
            stack = []
            for i in message:
                stack.append(i)
            # reverse stack so it pops in the right order
            stack.reverse()

            # for loops navigate to each byte of the array
            for a in range(len(image)):
                for b in range(len(image[a])):
                    for c in range(len(image[a,b])):
                        if stack != []:
                            # byte converted to binary and LSB is changed based on encoded message
                            lsb = bin(image[a,b,c])
                            final = lsb[:-1] + str(stack.pop())
                            image[a,b,c] = int(final[2:],2)
            cv2.imwrite(fileout, image)
            
    # decodes an image based on specified codec
    def decode(self, filein, codec):
        image = cv2.imread(filein)  
        flag = True 
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            message = ''
            # navigates to each byte in the array, converts to a binary number, and extracts the lsb
            for a in range(len(image)):
                for b in range(len(image[a])):
                    for c in range(len(image[a,b])):
                        byte = bin(image[a,b,c])
                        bit = byte[-1]
                        message += bit
            binary_data = message
    
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = binary_data           
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

