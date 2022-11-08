from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class Sortable (ABC):

    @abstractmethod
    def sort (self) -> None:
        """
        :rtype: None
        """
        pass