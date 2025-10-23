"""
Handle and encapsulate some of the logic for mngmt

"""
from enum import Enum, auto


class _QDiff(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class _QAttrs(Enum):





class NeetCodeSection:
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"num_questions={getattr(self, 'num_questions', 0)}/"
            f"{getattr(self, 'count_neetcode', '?')}, "
            f"list={getattr(self, 'list_questions', [])})")


def easy_q(func):
    """Defines the question as easy, print for now."""
    def medium(*args, **kwargs):
        difficulty: _QDiff = _QDiff.EASY
        print(f"This is an {difficulty} exercise.")
        result = func(*args, **kwargs)
        return result

    return medium


def medium_q(func):
    """Defines the question as medium, print for now."""
    def medium(*args, **kwargs):
        difficulty: _QDiff = _QDiff.MEDIUM
        print(f"This is an {difficulty} exercise.")
        result = func(*args, **kwargs)
        return result

    return medium


def hard_q(func):
    """Defines the question as hard, print for now."""
    def hard(*args, **kwargs):
        difficulty: _QDiff = _QDiff.HARD
        print(f"This is an {difficulty} exercise.")
        result =func(*args, **kwargs)
        return result
    return hard

def has_inner_class(func):
    """Specifies that a question contains a class definition inside of it"""
    def inner(*args, **kwargs):
        print("This method has a class defined inside of it.")
        result = func(*args, **kwargs)
        return result
    return inner

