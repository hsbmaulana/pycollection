import unittest
import pytest
from Pycollection.Trees.BinarySearchTree import BinarySearchTree

class TestBinarySearchTree (unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """

        self.__collection = BinarySearchTree ()

        self.__collection.add (10)
        self.__collection.add (20)
        self.__collection.add (30)
        self.__collection.add (40)
        self.__collection.add (50)

        yield

        self.__collection = None

    def test_add (self) -> None:
        """
        :rtype: None
        """
        # self.__collection.breadth ()
        # self.__collection.depth ()

        self.assertTrue (True)

    def test_contain (self) -> None:
        """
        :rtype: None
        """
        self.assertTrue (self.__collection.contain (30))