from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class ITree (ABC):

    @abstractmethod
    def add (self, value: int) -> None:
        """
        :type value: int
        :rtype: None
        """
        pass

    @abstractmethod
    def contain (self, value: int) -> bool:
        """
        :type value: int
        :rtype: bool
        """
        pass

    @abstractmethod
    def breadth (self) -> None:
        """
        :rtype: None
        """
        pass

    @abstractmethod
    def depth (self) -> None:
        """
        :rtype: None
        """
        pass