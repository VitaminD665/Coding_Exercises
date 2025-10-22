""" Module to encapsulate the problems
 on two"""

from scaffolding import MemberCountingMeta
from typing import override

class TwoPointers(metaclass=MemberCountingMeta):
    """
    Encapsulate the methods and exercises complete in this class

    """
    count_neetcode: int = 5

    @override
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"num_questions_solved={self.num_questions}, "
                f"out_of={self.count_neetcode}, "
                f"list={self.list_questions})")

