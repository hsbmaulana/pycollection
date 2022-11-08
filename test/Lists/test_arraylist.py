import unittest
import pytest
from Pycollection.Lists.ArrayList import ArrayList

class TestArrayList (unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """

        self.__collection = ArrayList ()

        self.__collection.add ("A")
        self.__collection.add ("B")
        self.__collection.add ("C")
        self.__collection.add ("D")
        self.__collection.add ("E")

        yield

        self.__collection = None

    def test_add (self) -> None:
        """
        :rtype: None
        """
        iterator = self.__collection.iterate ()

        while (iterator.hasNext ()):

            self.assertIn (iterator.next (), ["A", "B", "C", "D", "E"])

    def test_count (self) -> None:
        """
        :rtype: None
        """
        self.assertEqual (self.__collection.count (), 5)

    def test_get (self) -> None:
        """
        :rtype: None
        """
        self.assertEqual (self.__collection.get (4), "E")

    def test_modify (self) -> None:
        """
        :rtype: None
        """
        self.__collection.modify (4, "XYZ")

        self.assertNotEqual (self.__collection.get (4), "E")

    def test_remove (self) -> None:
        """
        :rtype: None
        """
        self.__collection.remove (4)
        self.assertNotEqual (self.__collection.get (4), "E")

        self.__collection.remove (3)
        self.assertNotEqual (self.__collection.get (3), "D")

        self.__collection.remove (2)
        self.assertNotEqual (self.__collection.get (2), "C")

        self.__collection.remove (1)
        self.assertNotEqual (self.__collection.get (1), "B")

        self.__collection.remove (0)
        self.assertNotEqual (self.__collection.get (0), "A")

        self.assertEqual (self.__collection.count (), 0)