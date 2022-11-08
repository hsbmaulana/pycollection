from typing import Union, Tuple, Optional, Any, cast
from .Graph import Graph

class DirectedGraph (Graph):

    def addEdge (self, row: int, column: int, weight: int) -> None:
        """
        :type row: int
        :type column: int
        :type weight: int
        :rtype: None
        """
        self.edges[row][column] = weight

    def removeEdge (self, row: int, column: int) -> None:
        """
        :type row: int
        :type column: int
        :rtype: None
        """
        self.edges[row][column] = 0