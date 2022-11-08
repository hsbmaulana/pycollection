from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast
from .Iterateable import Iterateable

class IList (ABC):

    @abstractmethod
    def add (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        pass

    @abstractmethod
    def count (self) -> int:
        """
        :rtype: int
        """
        pass

    @abstractmethod
    def get (self, index: int) -> Tuple[int, str, None]:
        """
        :type index: int
        :rtype: Tuple[int, str, None]
        """
        pass

    @abstractmethod
    def iterate (self) -> Iterateable:
        """
        :rtype: Iterateable
        """
        pass

    @abstractmethod
    def modify (self, index: int, value: Union[int, str]) -> None:
        """
        :type index: int
        :type value: Union[int, str]
        :rtype: None
        """
        pass

    @abstractmethod
    def remove (self, index: int) -> None:
        """
        :type index: int
        :rtype: None
        """
        pass