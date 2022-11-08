import unittest
import pytest

class TestCase (unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """

        print ("The setup.")

        yield

        print ("The teardown.")

    def test_case (self) -> None:
        """
        :rtype: None
        """
        print ("The case.")