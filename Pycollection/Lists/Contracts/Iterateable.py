from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class Iterateable (ABC):

    @abstractmethod
    def hasNext (self) -> bool:
        """
        :rtype: bool
        """
        pass

    @abstractmethod
    def next (self) -> Tuple[int, str, None]:
        """
        :rtype: Tuple[int, str, None]
        """
        pass