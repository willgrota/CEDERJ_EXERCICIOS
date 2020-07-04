
from __future__ import print_function


import sys
from random import randint

## Compare two objects.
 #
 # @return (x > y) - (x < y)
 #
def cmp(x, y):
     return (x > y) - (x < y)


class BalancedBSTSet(object):
     #
    class Node(object):
         #  Constructor given a data object and the parent of this node.
        def __init__(self, key, parent=None):
            ## Data (object) in this node.
            self.data = key
            ## Reference to the parent node.
            self.parent = parent
            ## Reference to the quantity node.
            self.counter = 0
            ## Reference to the left child node.   
            self.left = None
            ## Reference to the right child node.
            self.right = None



        ## Return a string representation of this node.
        def __str__(self):
            return str(self.data) + " " + str(self.counter)

        ## Return a string representation of this node.             
        def __repr__(self):
             return "Node: %s, Size: %d" % \
                   (self.data, sys.getsizeof(self))

        ## Compares the data of this node to a given key.
        #  return 1 if the data of this object is greater than key's, <br>
        #         -1 if the data of this object is smaller than key's or <br>
        #          0 if it is equal
        def compareTo(self,key):
            return cmp(self.data,key)

    ##
     # Constructs an empty binary search tree.
    def __init__(self , self_balancing =False , top =0, bottom =0):
        ## Root of this tree.
        self.__root = None
        ## Number of elements in this tree.
        self.__size = 0
        self.self_balancing = self_balancing

        if self_balancing:
            if bottom == 0:
                self.top = 2
                self.bottom = 3
            else:
                self.top = top
                self.bottom = bottom


    #
    def getcounter(self, key):
        current = self.__root
        while True:
            comp = current.compareTo(key)
            if (comp == 0):
                return "Chave:", current.data, "Filho Esquerdo:", current.left, "Filho Direito:", current.right
            elif (comp > 0):
                if (current.left != None):
                    current = current.left
                else:
                    return current.counter
            else:
                if (current.right != None):
                    current = current.right
                else:
                    return current.counter



    def rebalance(self, bstNode):

        def make_tree(nodes, parent):
            if nodes.__len__()%2 == 0:
                middle = (((nodes.__len__()) // 2) - 1)
            else:
                middle = ((nodes.__len__()) // 2)

            node = nodes[middle]
            node.parent = parent
            node.counter = nodes.__len__()

            if middle >= 1:
                nodes_left = nodes[0: middle]
                nodes_right = nodes[middle+1 : nodes.__len__()]
                node.left = make_tree(nodes_left, node)
                node.right = make_tree(nodes_right, node)
            else:
                if nodes.__len__() > 1:
                    node.left = None
                    nodes_right = nodes[1:2]
                    node.right = make_tree(nodes_right, node)
                else:
                    node.left = None
                    node.right = None
            return node

        if bstNode == None: return
        node_parent = bstNode.parent
        node_list = []
        self.__inOrder(bstNode, node_list)
        subtree_root = make_tree(node_list, bstNode.parent)

        if subtree_root.parent == None:
            self.__root = subtree_root
        elif node_parent.left == bstNode:
            node_parent.left = subtree_root
        else:
            node_parent.right = subtree_root


     # Returns a read-only view of the root node of this tree.
    def root(self):
        return self.__root

    ## Return whether this tree is empty.
    def isEmpty(self):
        return self.__root is None


     #  Executes an in order traversal of the tree rooted at a given node.
    def __inOrder ( self, node, arr ):
        if arr is None: arr = []
        if ( node != None ):
            self.__inOrder ( node.left, arr )
            arr.append ( node )
            self.__inOrder ( node.right, arr )
        return arr


     # Returns whether the given object is in this tree.
    def __contains__(self, obj):
        return self.findEntry(obj) != None


     # Adds the given object to this tree.
    def add(self, key):
        if self.__root is None:
            self.__root = self.Node(key, None)
            self.__size += 1
            self.__root.counter += 1
            return True

        current = self.__root
        while True:
            comp = current.compareTo(key)
            if (comp == 0):
                # key is already in the tree
                return False
            elif (comp > 0):
                if (current.left != None):
                    current = current.left
                else:
                    current.left = self.Node(key, current)
                    current.left.counter += 1
                    self.count_node(current, 1)
                    self.__size += 1

                    if self.self_balancing:
                        unbalanced_node = self.find_unbalanced(current)
                        if unbalanced_node != None:
                            self.rebalance(unbalanced_node)
                    return True
                    
            else:
                if (current.right != None):
                    current = current.right
                else:
                    current.right = self.Node(key, current)
                    current.right.counter += 1
                    self.count_node(current, 1)
                    self.__size += 1

                    if self.self_balancing:
                        unbalanced_node = self.find_unbalanced(current)
                        if unbalanced_node != None:
                            self.rebalance(unbalanced_node)
                    return True


    ## Adds an iterable to the tree.
    def update(self,lst):
        for i in lst:
            self.add ( i )

    ## like lists.
    def append(self, n):
        return self.add(n)
                

     # Removes the given object from this tree.
    def remove(self, obj):
        n = self.findEntry(obj)
        if n == None:
            return False
        parent = n.parent
        self.unlinkNode(n)
        self.count_node(parent, -1)

  # update counters
        if self.self_balancing:
            unbalanced_node = self.find_unbalanced(parent)
            if unbalanced_node != None:
                #print (unbalanced_node)
                self.rebalance(unbalanced_node)
        return True
    

     # Returns the node containing key, or None if the key is not
    def find_unbalanced(self, parent):
        atual = parent
        unbalanced = None
        if atual != None:
            while True:
                if atual.left == None:
                    left = 0
                else:
                    left = atual.left.counter
                if atual.right == None:
                    right = 0
                else:
                    right = atual.right.counter
                if (left*self.bottom > atual.counter*self.top) or (right*self.bottom > atual.counter*self.top):
                    unbalanced = atual

                if atual.parent == None:
                    return unbalanced
                else:
                    atual = atual.parent

    def count_node(self, parent, inc):
        atual = parent
        if atual != None:
            while atual.parent != None:
                atual.counter += inc
                atual = atual.parent
            atual.counter += inc


    def findEntry(self, key):
        current = self.__root
        while (current != None):
            comp = current.compareTo(key)
            if (comp == 0):
                return current
            elif (comp > 0):
                current = current.left
            else:
                current = current.right
        return None


     # Returns the successor of the given node.
    def successor(self, n):
        if (n == None):
            return None
        elif (n.right != None):
            # leftmost entry in right subtree
            current = n.right
            while (current.left != None):
                current = current.left
            return current
        else:
            # we need to go up the tree to the closest ancestor that is
            # a left child its parent must be the successor
            current = n.parent
            child = n
            while (current != None and current.right == child):
                child = current
                current = current.parent
            # either current is None, or child is left child of current
            return current


     # Removes the given node, preserving the binary search
    def unlinkNode(self, n):
        # first deal with the two-child case copy
        # data from successor up to n, and then delete successor 
        # node instead of given node n startNode = None
        if (n.left != None and n.right != None):
            s = self.successor(n)
            n.data = s.data
            n = s # causes s to be deleted in code below startNode = s.parent

        # n has at most one child
        replacement = None    
        if (n.left != None):
            replacement = n.left
        elif (n.right != None):
            replacement = n.right

        # link replacement on tree in place of node n 
        # (replacement may be None)
        if (n.parent == None):
            self.__root = replacement
        else:
            if (n == n.parent.left):
                n.parent.left = replacement
            else:
                n.parent.right = replacement

        if (replacement != None):
            replacement.parent = n.parent
        
        self.__size -= 1
    
    ## Returns an iterator for this tree.
    def iterator(self):
        return self.BSTIterator(self)
    
    ## Returns the number of elements in this tree.
    def __len__(self):
        return self.__size

    ## Returns an array containing all of the elements in this tree. 
     # If the collection makes any guarantees as to what order its elements 
     # are returned by its iterator, this method must return the elements in the same order.
    def toArray(self):
        arr = []
        for n in self.iterator():
            arr.append(n)
        return arr

    ## Indexing operator [].
    def __getitem__(self, ind):
        if ind < 0 or ind >= self.__size:
           raise IndexError

        for i,n in enumerate(self.iterator()):
            if i == ind:
               return n

    ## Iterator as a generator.
    def __iter__(self):
        for n in self.iterator():
            yield n

    ## Return the height of this tree.
    def height(self):
        return self.getHeight(self.__root)

    ## Return the height of a subtree.
    def getHeight(self, root):
       if root != None:
          return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
       else:
          return -1
    

     # Returns a representation of this tree as a multi-line string.
    def __repr__(self):
        sb = []
        self.__toStringRec(self.__root, sb, 0)
        return ''.join(sb)

    ## Prints the nodes of this tree in order.
    def __str__(self):
        st = ""
        for n in self:
            st += str(n) + " "
        return st


     # Preorder traversal of the tree that builds a string representation
     # in the given StringBuilder.
    def __toStringRec(self, n, sb, depth):
        sb.append("  "*depth)
        
        if n is None:
            sb.append("-\n")
            return
        
        if (n.left is not None or n.right is not None):
            sb.append("+ ")
        else:
            sb.append("- ")
     
        sb.append(str(n))
        sb.append("\n")
        if (n.left is not None or n.right is not None):
            self.__toStringRec(n.left, sb, depth + 1)   
            self.__toStringRec(n.right, sb, depth + 1)


     # Iterator implementation for this binary search tree. The elements
     # are returned in ascending order according to their natural ordering.
    class BSTIterator(object):
        ## return the smallest value of the tree.
        def getSmallestValue(self,n):
            if (n != None):
                while (n.left != None):
                       n = n.left
            return n


         # Constructs an iterator starting at the smallest
         # ot largest element in the tree.
        def __init__(self, tree):
            ## Node returned by last call to next() and available
            #  for removal. This field is None when no node is
            #  available to be removed.
            self.__pending = None

            ## The tree to be traversed.
            #  Inner classes do not have access to outer class variables.
            self.__tree = tree

            ## Node to be returned by next call to next().
            self.__current = self.getSmallestValue(self.__tree.root())

        ## Forward iterator.
        def __iter__(self):
            # start out at smallest value
            self.__current = self.getSmallestValue(self.__tree.root())
            return self

        ##
         # Whether current is not None.
        def hasNext(self):
            return self.__current != None

        ## Return the content of the current node without advancing.
        def peek(self):
            if self.__current is None:
               return None
            return self.__current.data


         # Returns current node, which is saved in pending.
         # Current is set to successor(current).
        def __next__(self):
            if (not self.hasNext()): raise StopIteration
            self.__pending = self.__current
            self.__current = self.__tree.successor(self.__current)
            return self.__pending.data

        ## For python 2.
        def next(self):
            return self.__next__()


         # Removes the node returned by the last call to next().
        def remove(self):
            if self.__pending is None: raise IndexError

            if (self.__pending.left != None and self.__pending.right != None):
                self.__current = self.__pending
            
            self.__tree.unlinkNode(self.__pending)
            self.__pending = None


 #  Generates an array with a random size,
 #  filled with random elements.
def generateRandomArray ( n, vrange ):
    v = []
    for i in range(randint(1,n)):
        v.append (randint(1,vrange))
    return v


##  
 #  Main function for testing.
 #  args not used.
def main ( args = None ):
    if args is None:
       args = sys.argv

    arr1 = [5,4,2,16,10,7,20,14,15,12]
    arr2 = generateRandomArray(15,500)
    arr3 = generateRandomArray(20,500)
    arr4 = generateRandomArray(20,50)
    arr5 = generateRandomArray(20,90)
    arr6 = [52,22,47,42,51,38,39,28]  # meu array

    arr = arr5
    bst = BalancedBSTSet(self_balancing=True)
    for i in arr:
        bst.add ( i )
        
    print("Original tree: height = %d\n%r" % (bst.height(),bst))

    a = bst.toArray()
    print ("toArray:")
    for i in a:
        print("%s, " % i, end="")
    print( "\b\b: size = %d, len = %d" % (len(a), len(bst)) )

    print("\nKeys in ascending order:")
    print ( bst )
   
    #if len(bst) > 3:
       #print("\n\nbst[3] = %d" % bst[3])

#----------------------------------------------------
    print("root =", bst.root())
    for i in bst:
        print(bst.getcounter(i))
# ----------------------------------------------------


    nid = 0
    while ( not bst.isEmpty() and nid >= 0 ):
            try:
                nid = int(input("Choose a node to delete: "))

            except (ValueError, SyntaxError) as e:
                print(e)
                continue
            except KeyboardInterrupt:
                sys.exit("The end.")
            
            if nid >= 0:
                bst.remove (nid)
                print("Removed node %d: height = %d\n%r"% (nid,bst.height()))


 # ----------------------------------------------------
                print("root =", bst.root())
                for i in bst:
                    print(bst.getcounter(i))
#----------------------------------------------------


if __name__=="__main__":
   main()
