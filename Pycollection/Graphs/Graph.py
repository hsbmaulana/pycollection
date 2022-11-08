from typing import Union, Tuple, Optional, Any, cast
from .Contracts.IGraph import IGraph

class Graph (IGraph):

    def __init__ (self, capacity: int = 10) -> None:
        """
        :type capacity: int
        :rtype: None
        """

        """ :vertices: List[int, str] """
        self.vertices = []

        """ :edges: List[int] """
        self.edges = []

        i = 0

        while (i < capacity):

            self.edges.insert(i, [])

            j = 0

            while (j < capacity):

                self.edges[i].insert(j, 0)
                j+=1

            i+=1

    def __del__ (self) -> None:
        """
        :rtype: None
        """

    def push (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        self.vertices.append (value)

    def pop (self) -> None:
        """
        :rtype: None
        """
        i = 0
        last = len (self.vertices) - 1

        while (i <= last):

            self.removeEdge (last, i)
            i+=1

        self.vertices.pop (-1)

    def enqueue (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        self.vertices.insert (0, value)

    def dequeue (self) -> None:
        """
        :rtype: None
        """
        i = 0
        first = 0
        last = len (self.vertices) - 1

        while (i <= last):

            self.removeEdge (first, i)
            i+=1

        self.vertices.pop (0)

    def breadth (self, edged: int) -> None:
        """
        :type edged: int
        :rtype: None
        """
        queue = [edged]
        log = []

        while (len (queue) > 0):

            front = queue.pop (0)
            rear = None
            log.append (front)

            print (self.vertices[front])

            i = 0

            while (i < len (self.vertices)):

                if (self.edges[front][i] != 0 and bool (i not in log)):

                    queue.append (i)

                i+=1

    def depth (self, edged: int) -> None:
        """
        :type edged: int
        :rtype: None
        """
        log = []
        reference = self

        def recurse (i):

            log.append (i)

            j = 0

            while (j < len (reference.vertices)):

                if (reference.edges[i][j] != 0 and bool (i not in log)):

                    recurse (j)

                j+=1

            print (reference.vertices[i])

        recurse (edged)