from typing import Union, Tuple, Optional, Any, cast
from .Contracts.ITree import ITree

class BinarySearchTree (ITree):

    def __init__ (self, value: Optional[int] = None) -> None:
        """
        :type value: Optional[int]
        :rtype: None
        """

        """ :left: Optional[BinarySearchTree] """
        self.left = None

        """ :right: Optional[BinarySearchTree] """
        self.right = None

        """ :value: Optional[int] """
        self.value = value

    def __del__ (self) -> None:
        """
        :rtype: None
        """

    def add (self, value: int) -> None:
        """
        :type value: int
        :rtype: None
        """
        if self.value == None:

            self.value = value

            return None

        if value > self.value:

            if self.right:

                self.right.add (value)

            else:

                self.right = BinarySearchTree ()
                self.right.add (value)

        else:

            if self.left:

                self.left.add (value)

            else:

                self.left = BinarySearchTree ()
                self.left.add (value)

    def contain (self, value: int) -> bool:
        """
        :type value: int
        :rtype: bool
        """
        if value == self.value:

            return True

        if value > self.value:

            if self.right:

                return self.right.contain (value)

            else:

                return False

        else:

            if self.left:

                return self.left.contain (value)

            else:

                return False

    def breadth (self) -> None:
        """
        :rtype: None
        """
        queue = [self]

        while (len (queue) > 0):

            front = queue.pop (0)
            rear = None

            print (front.value)

            if front.left:

                queue.append (front.left)

            if front.right:

                queue.append (front.right)

    def depth (self) -> None:
        """
        :rtype: None
        """
        if self.left:

            self.left.depth ()

        print (self.value)

        if self.right:

            self.right.depth ()