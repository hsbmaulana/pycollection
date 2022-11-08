from typing import Union, Tuple, Optional, Any, cast
from .Contracts.IList import IList
from .Contracts.Iterateable import Iterateable
from .Contracts.Sortable import Sortable
from .Contracts.Searchable import Searchable

class LinkedList (IList, Sortable, Searchable):

    def __init__ (self) -> None:
        """
        :rtype: None
        """

        """ :__length: int """
        self.__length = 0

        """ :head: Optional[Node] """
        self.head = None

        """ :foot: Optional[Node] """
        self.foot = None

    def __del__ (self) -> None:
        """
        :rtype: None
        """

    class Node:

        def __init__ (self, value: Union[int, str]) -> None:
            """
            :type value: Union[int, str]
            :rtype: None
            """

            """ :previous: Optional[Node] """
            self.previous = None

            """ :next: Optional[Node] """
            self.next = None

            """ :value: Union[int, str] """
            self.value = value

        def __del__ (self) -> None:
            """
            :rtype: None
            """

    def add (self, value: Union[int, str]) -> None:
        """
        :type value: Union[int, str]
        :rtype: None
        """
        if self.head == None:

            self.head = self.Node (value)
            self.foot = self.head

            self.__length+=1

        else:

            current = self.head

            while (current.next):

                current = current.next

            current.next = self.Node (value)
            current.next.previous = current

            self.foot = current.next
            self.__length+=1

    def count (self) -> int:
        """
        :rtype: int
        """
        return self.__length

    def get (self, index: int) -> Tuple[int, str, None]:
        """
        :type index: int
        :rtype: Tuple[int, str, None]
        """
        if index >= 0 and index < self.count ():

            iterator = self.iterate ()
            i = 0

            while (iterator.hasNext ()):

                value = iterator.next ()

                if i == index:

                    return value

                i+=1

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

                """ :iterator: Optional[Node] """
                self.iterator = state.head

            def __del__ (self) -> None:
                """
                :rtype: None
                """

            def hasNext (self) -> bool:
                """
                :rtype: bool
                """
                return self.iterator != None

            def next (self) -> Tuple[int, str, None]:
                """
                :rtype: Tuple[int, str, None]
                """
                if self.hasNext ():

                    value = self.iterator.value
                    self.iterator = self.iterator.next

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

            iterator = self.iterate ()
            i = 0

            while (iterator.hasNext ()):

                node = iterator.iterator

                if i == index:

                    node.value = value
                    return None

                iterator.next ()
                i+=1

    def remove (self, index: int) -> None:
        """
        :type index: int
        :rtype: None
        """
        if index >= 0 and index < self.count ():

            iterator = self.iterate ()
            i = 0

            while (iterator.hasNext ()):

                node = iterator.iterator

                if i == index:

                    if node.previous and node.next:

                        node.previous.next = node.next
                        node.next.previous = node.previous

                    elif node.previous and node.next == None:

                        node.previous.next = None
                        self.foot = node.previous

                    elif node.previous == None and node.next:

                        node.next.previous = None
                        self.head = node.next

                    elif node.previous == None and node.next == None:

                        iterator.iterator = None
                        node = None
                        self.head = node
                        self.foot = node

                    self.__length-=1

                    return None

                iterator.next ()
                i+=1

    def sort (self) -> None:
        """
        :rtype: None
        """

    def search (self) -> Tuple[int, str, None]:
        """
        :rtype: Tuple[int, str, None]
        """