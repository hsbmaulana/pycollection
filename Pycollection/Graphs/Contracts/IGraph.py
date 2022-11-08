from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class IGraph (ABC):

    @abstractmethod
    def push (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        pass

    @abstractmethod
    def pop (self) -> None:
        """
        :rtype: None
        """
        pass

    @abstractmethod
    def enqueue (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        pass

    @abstractmethod
    def dequeue (self) -> None:
        """
        :rtype: None
        """
        pass

    @abstractmethod
    def addEdge (self, row: int, column: int, weight: int) -> None:
        """
        :type row: int
        :type column: int
        :type weight: int
        :rtype: None
        """
        pass

    @abstractmethod
    def removeEdge (self, row: int, column: int) -> None:
        """
        :type row: int
        :type column: int
        :rtype: None
        """
        pass

    @abstractmethod
    def breadth (self, edged: int) -> None:
        """
        :type edged: int
        :rtype: None
        """
        pass

    @abstractmethod
    def depth (self, edged: int) -> None:
        """
        :type edged: int
        :rtype: None
        """
        pass