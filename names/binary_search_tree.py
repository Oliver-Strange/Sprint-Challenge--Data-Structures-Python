import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # need to traverse to find spot to insert
    def insert(self, value):
        '''
        current_node = self
        looking = True
        while looking:
              if value is < node.value and node.left:
                    current_node = node.value.left
              elif value is >= nod.value and node.right:
                    current_node = node.value.right
              elif value is < node.value and node.value.left is None:
                    node.value.left = BinarySearchTree(value)
                    looking = false
              elif value is >= node.value and node.value.right is None:
                    node.value.right = BinarySearchTree(value)
                    looking = false

        '''
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
# set current node as self
# while something is true
# if value is < than node.value and there is a node.left
        # set current node = node.value.left
# else/if value is >= node.value and there is a node.right
        # set current node = node.value.right
# else/if value is < than current node.value and there is no current node.left
        # make a new BST with the value
# else/if value is >= current node.value and there is no current node.right
        # make a new BST with the value

    # `contains` searches the binary search tree for the input value, returning
    # a boolean indicating whether the value exists in the tree or not.
    # starts at root and traverse the tree
    # stop at first instance of a value
    # is not found if we get to a node that doesn't have children
    def contains(self, target):

        if self.value == target:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)


# check if current value is target, if so, done
# otherwise left or right depending on value
# call contains - recursion

    # `get_max` returns the maximum value in the binary search tree.
    # max is farthest to the right


    def get_max(self):
          # recursive
        if not self.right:
            return self.value
        return self.right.get_max()

        '''
        # iterative
        max_value = self.value
        current = self
        while current:
              max_value = current.value
              current = current.right

        return max_value
        '''

        '''
        iterative
        variable = self
        while variable.right is not None:
              variable = variable.right
        return variable.value
        '''

    # `for_each` performs a traversal of _every_ node in the tree, executing the
    # passed-in callback function on each tree node value. There is a myriad of
    # ways to perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


'''
 # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_dft(self, node):
        if node.left:
            node.in_order_dft(node.left)
        print(node.value)
        if node.right:
            node.in_order_dft(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        current_node = node
        while q.size > 0:
            current_node = q.dequeue()
            print(current_node.value)
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        current_node = node
        while s.size > 0:
            current_node = s.pop()
            print(current_node)
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
'''
