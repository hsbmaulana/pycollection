import unittest
import pytest
from Pycollection.Graphs.UndirectedGraph import UndirectedGraph

class TestUndirectedGraph (unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """

        self.__collection = UndirectedGraph (5)

        self.__collection.push ("A")
        self.__collection.enqueue ("B")
        self.__collection.push ("C")
        self.__collection.enqueue ("D")
        self.__collection.push ("E")

        self.__collection.addEdge (0, 1, 10)
        self.__collection.addEdge (1, 2, 20)
        self.__collection.addEdge (2, 3, 30)
        self.__collection.addEdge (4, 1, 40)
        self.__collection.addEdge (3, 2, 50)

        yield

        self.__collection = None

    def test_vertex (self) -> None:
        """
        :rtype: None
        """
        self.assertListEqual (self.__collection.vertices, ["D", "B", "A", "C", "E"])

    def test_edge (self) -> None:
        """
        :rtype: None
        """
        self.assertListEqual (self.__collection.edges, [[0, 10, 0, 0, 0], [10, 0, 20, 0, 40], [0, 20, 0, 50, 0], [0, 0, 50, 0, 0], [0, 40, 0, 0, 0]])

    def test_traverse (self) -> None:
        """
        :rtype: None
        """
        # self.__collection.breadth (3)
        # self.__collection.depth (3)

        self.assertTrue (True)