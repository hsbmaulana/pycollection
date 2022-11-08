from typing import Union, Tuple, Optional, Any, cast
from .Contracts.IList import IList
from .Contracts.Iterateable import Iterateable
from .Contracts.Sortable import Sortable
from .Contracts.Searchable import Searchable

class ArrayList (IList, Sortable, Searchable):

    def __init__ (self) -> None:
        """
        :rtype: None
        """

        """ :__index: int """
        self.__index = 0

        """ :__capacity: int """
        self.__capacity = 10

        """ :__list: List[int, str, None] """
        self.__list = [None] * self.__capacity

    def __del__ (self) -> None:
        """
        :rtype: None
        """

    def add (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        if self.count () == self.__capacity:

            capacity  = self.__capacity * 2
            temporary = [None] * capacity

            i = 0

            while (i < self.__capacity):

                temporary[i] = self.__list[i]
                i+=1

            self.__capacity = capacity
            self.__list = temporary

        self.__list[self.__index] = value
        self.__index+=1

    def count (self) -> int:
        """
        :rtype: int
        """
        return self.__index

    def get (self, index: int) -> Tuple[int, str, None]:
        """
        :type index: int
        :rtype: Tuple[int, str, None]
        """
        if index >= 0 and index < self.count ():

            return self.__list[index]

        return None

    def iterate (self) -> Iterateable:
        """
        :rtype: Iterateable
        """
        state = self

        class Iterator (Iterateable):

            def __init__ (self) -> None:
                """
                :rtype: None
                """

                """ :iterator: int """
                self.iterator = 0

            def __del__ (self) -> None:
                """
                :rtype: None
                """

            def hasNext (self) -> bool:
                """
                :rtype: bool
                """
                return self.iterator < state.count ()

            def next (self) -> Tuple[int, str, None]:
                """
                :rtype: Tuple[int, str, None]
                """
                if self.hasNext ():

                    value = state.get (self.iterator)
                    self.iterator+=1

                    return value

                return None

        return Iterator ()

    def modify (self, index: int, value: Union[int, str]) -> None:
        """
        :type index: int
        :type value: Union[int, str]
        :rtype: None
        """
        if index >= 0 and index < self.count ():

            self.__list[index] = value

    def remove (self, index: int) -> None:
        """
        :type index: int
        :rtype: None
        """
        if index >= 0 and index < self.count ():

            while (self.__list[index + 1] != None):

                self.__list[index] = self.__list[index + 1]
                index+=1

            self.__index-=1
            del self.__list[self.__index]

    def sort (self) -> None:
        """
        :rtype: None
        """

    def search (self) -> Tuple[int, str, None]:
        """
        :rtype: Tuple[int, str, None]
        """