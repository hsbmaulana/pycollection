from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class Searchable (ABC):

    @abstractmethod
    def search (self) -> Tuple[int, str, None]:
        """
        :rtype: Tuple[int, str, None]
        """
        pass