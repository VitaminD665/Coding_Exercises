"""
Handle and encapsulate some of the logic for mngmt

"""


class NeetCodeSection:
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"num_questions={getattr(self, 'num_questions', 0)}/"
            f"{getattr(self, 'count_neetcode', '?')}, "
            f"list={getattr(self, 'list_questions', [])})")