################################################################################
#                         Balanced Binary Tree                                 #
# Given a sorted (increasing order) array, write an algorithm                  #
# to create a binary tree with minimal height                                  #
################################################################################

def getBalancedBinaryTree(sortedArray):
    """insert in a balanced tree elements from a sortedArray"""
    nbElements = len(sortedArray)
    if  nbElements != 0:
        for i in range(0, nbElements//2):
            print("Subtree of root {}".format(sortedArray[i]))
            if 2*i+1 < nbElements:
                print("Left Child {}".format(sortedArray[2*i+1]))
            if 2*i+2 < nbElements:
                print("Right Child {}".format(sortedArray[2*i+2]))


array = [1,2,7,9,12]
getBalancedBinaryTree(array)

        
    
