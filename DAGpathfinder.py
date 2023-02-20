''' This is an assignment I worked on as part of BME 205, a graduate level programming class where we use DP to find the longest Path in a Directed Acyclic Graph'''
# input: A start node, end node, and list of edges
# returns the path of greatest value from start node to end node and the value of the path
# Groupmates: Alan Faber, Sarah Ghasemi
# Author: Jeffrey Jacob

class DAG:
    def __init__(self, begin, end):
        ''' Constructor, saves the beginning point of the graph and the end point '''
        self.begin = begin
        self.end = end
        

    def CreateNodeDict(self, UnusedEdgeList, NodesList):
        ''' 
        Creates a dictionary of the nodes that have an edge that either comes from them or have an edge that leads to them.
        The dictionary contains a list for every node that has information on each node.
        The information is: [max value, the node previous that led to the maximum value, if the node is prepared, and number of unused edges that lead to the node]
        '''
        NodeDict = {}
        for edge in UnusedEdgeList:
            # The values 0, 0, False, 0 are placeholders for maxValue, backtracking pointer, preparedness, # of inputs, and list of inputs
            if edge[0] not in NodesList:
                NodesList.append(edge[0])
                NodeDict[edge[0]] = [0, 0, False, 0, []]
            if edge[1] not in NodesList:
                NodesList.append(edge[1])
                NodeDict[edge[1]] = [0, 0, False, 0, []]
        return NodeDict

    def MakeBeginAndEndChanges(self, NodeDict, NodesList, UnusedEdgesList, begin, end):
        '''
        Modifies the NodeDict: Changes the beginning node to prepared.
        Removes edges that lead to the begin node and edges that leave the end node.
        '''
        # set beginning node's values, remove node from Unused list, and add node to Used list
        NodeDict[begin][0] = 0
        NodeDict[begin][1] = False
        NodeDict[begin][2] = True
        NodesList.remove(begin)
        # Check for nodes that aren't the start node and have no inputs. Set their max value to -2000 so they aren't used.
        for node in NodesList:
            flag = False
            for edge in UnusedEdgesList:
                if edge[1] == node:
                    flag = True
            if flag == False:
                NodeDict[node][0] = -2000
                NodeDict[node][2] = True

        # Go through all edges that leave the end node or go into the begin node and remove them from the list
        listOfUnuseableEdges = []
        for edge in UnusedEdgesList:
            if edge[0] == end:
                listOfUnuseableEdges.append(edge)
            if edge[1] == begin:
                listOfUnuseableEdges.append(edge)
        for edge in listOfUnuseableEdges:
            UnusedEdgesList.remove(edge)

    def AddPreparedEdges(self, UnusedEdgesList, NodeDict, PreparedEdgesList):
        ''' Add edges that have not been used and whose start point is prepared '''
        for edge in UnusedEdgesList:
            if NodeDict[edge[0]][2] == True:
                PreparedEdgesList.append(edge)

    def EvaluatePreparedEdges(self, PreparedEdgesList, NodeDict, UnusedEdgesList, UsedEdgesList):
        '''
        Evaluate each prepared edge to see if it leads to a higher maxVal for the end node, update the DictOfNodes if it
        does so with the new maxVal, the new backpointer, and number of inputs not evaluated. Remove edge from the list
        of unused edges and add it to the list of used edges. Clear the list of prepared edges afterwards.
        '''
        for edge in PreparedEdgesList:
            if (edge[2] + NodeDict[edge[0]][0]) > NodeDict[edge[1]][0]:
                NodeDict[edge[1]][0] = edge[2] + NodeDict[edge[0]][0]
                NodeDict[edge[1]][1] = edge[0]
            NodeDict[edge[1]][3] -= 1
            UnusedEdgesList.remove(edge)
            UsedEdgesList.append(edge)
        PreparedEdgesList.clear()

    def PrepareEdges(self, NodeDict):
        ''' Go through the list of edges checking for nodes that have 0 inputs that are unused and set the nodes to ready '''
        for node in NodeDict:
            # if node has 0 incoming unevaluated edges
            if NodeDict[node][3] == 0:
                NodeDict[node][2] = True

    def AddInputs(self, NodeDict, UnusedEdgesList):
        ''' Adds the possible inputs to the nodes '''
        for edge in UnusedEdgesList:
            NodeDict[edge[1]][4].append(edge[0])


def main(inFile = None):
    '''
    
    reads a file and parses ut, applies methods from the dag class to find the longest weighted path
    
    '''
    listOfNodes = []
    listOfUsedEdges = []
    listOfPreparedEdges = []
    listOfUnusedEdges = []
    
    with open(inFile) as fh:
        begin = int(fh.readline().rstrip())
        end = int(fh.readline().rstrip())
        thisDAG = DAG(begin, end)
        for line in fh:
            startNode =  0
            endNode = 0
            value = 0
            temp = ""
            # Requires a newline character on the last line to work for the last edge (txt file must have a blank line at the end)
            for char in line:
                if char == "-":
                    startNode = int(temp)
                    temp = ""
                    continue
                if char == ">":
                    continue
                if char == ":":
                    endNode = int(temp)
                    temp = ""
                    continue
                if char == '\n':
                    value = int(temp)
                    continue
                temp = temp + str(char)
            tempTup = (startNode, endNode, value)
            listOfUnusedEdges.append(tempTup)
        
        # Create the dictionary of nodes with the initial values
        dictOfNodes = thisDAG.CreateNodeDict(listOfUnusedEdges, listOfNodes)
        
        # Check for nodes that aren't the start point and have no inputs, if there are any, sets their max value to -2000     
        # Go through all edges that leave the end node or go into the start node and remove them from the list
        thisDAG.MakeBeginAndEndChanges(dictOfNodes, listOfNodes, listOfUnusedEdges, begin, end)
        
        
        # Go through all edges and add 1 to a Node's number of inputs to it in the DictOfNodes
        for edge in listOfUnusedEdges:
            dictOfNodes[edge[1]][3] += 1
            
        # Add all inputs to the list of inputs for each node in the dictionary of nodes
        thisDAG.AddInputs(dictOfNodes, listOfUnusedEdges)
        
        # If a node's edges only come from a node with a -2000 value, set node's value to -2000
        for node in dictOfNodes:
            flagg = False
            for inputs in dictOfNodes[node][4]:
                if dictOfNodes[inputs][0] > -2000:
                    flagg = True
            if node == begin:
                flagg = True
            if flagg == False:
                dictOfNodes[node][0] = -2000
        
        # iterate until all edges have been evaluated
        while listOfUnusedEdges:
            # Go through the list of edges checking for nodes that have 0 inputs that are unused and set the nodes to ready
            thisDAG.PrepareEdges(dictOfNodes)
            # Add edges that have not been used and whose start point is prepared
            thisDAG.AddPreparedEdges(listOfUnusedEdges, dictOfNodes, listOfPreparedEdges)
            # evaluate each prepared edge to see if it leads to a higher maxVal for the end node, update the DictOfNodes if it
            # does so with the new maxVal, the new backpointer, and number of inputs not evaluated. Remove edge from the list
            
            # of unused edges and add it to the list of used edges. 
            thisDAG.EvaluatePreparedEdges(listOfPreparedEdges, dictOfNodes, listOfUnusedEdges, listOfUsedEdges)
        
        
        print(dictOfNodes[end][0])
        
        
        
        path = []
        currentNode = end
        # get the path backwards and put in in a list
        while currentNode is not False:
            path.append(currentNode)
            currentNode = dictOfNodes[currentNode][1]
        path = path[::-1]
        
        # print out the path
        for x in range(len(path) - 1):
            print(str(path[x]) + "->", end="")
        print(path[len(path) - 1])
        
    

    
if __name__ == "__main__":
    main(inFile = 'rosalind_ba5d.txt') 
