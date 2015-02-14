#################################################################################
#                          List of Nodes per depth                              #
# Given a binary search tree, design an algorithm which creates a list of       #
# all the nodes at each depth                                                   #
#################################################################################

from binarySearchTree import BinarySearchTree, TreeNode

def getListofNodesPerDepth(bst):
    """returns a list at index i is the elements at depth i in the binary search tree bst"""
    nodesPerDepth = []
    nbVisitedNodes = 0
    nbNodes = len(bst)
    if nbNodes == 0:
        return []
    #at depth 0, only the root
    currentNodes = []
    currentNodes.append(bst.root)
    nodesPerDepth.append(currentNodes)
    nbVisitedNodes += 1
    # at depth current, newNodes at depth current+1 are their left and right children
    while (nbVisitedNodes < nbNodes):
        newNodes = []
        for treeNode in currentNodes:
            if treeNode.hasLeftChild():
                newNodes.append(treeNode.leftChild)
                nbVisitedNodes += 1
            if treeNode.hasRightChild():
                newNodes.append(treeNode.rightChild)
                nbVisitedNodes += 1
        nodesPerDepth.append(newNodes)
        currentNodes = newNodes
    return nodesPerDepth
    

##################
# Main() to test #
##################
if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree[5]="green"
    for i in mytree:
        print(i, mytree[i])

    nodesperDepth = getListofNodesPerDepth(mytree)
    if nodesperDepth == []:
        print("Tree is empty")
    else:
        for depth, nodes in enumerate(nodesperDepth):
            print("Depth {}".format(depth))
            for node in nodes:
                print("Key {} Payload {}".format(node.key, node.payload), end='   ')
            print()
            
        
