"""
Handle and encapsulate some of the logic for mngmt

"""
from enum import Enum, auto


class _QDiff(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class NeetCodeSection:
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"num_questions={getattr(self, 'num_questions', 0)}/"
            f"{getattr(self, 'count_neetcode', '?')}, "
            f"list={getattr(self, 'list_questions', [])})")


def easy_q(func):
    """Defines the question as easy, print for now."""
    def wrapper(*args, **kwargs):
        difficulty: _QDiff = _QDiff.EASY
        print(f"This is an {difficulty} exercise.")
        result = func(*args, **kwargs)
        return result

    return wrapper


def medium_q(func):
    """Defines the question as medium, print for now."""
    def wrapper(*args, **kwargs):
        difficulty: _QDiff = _QDiff.MEDIUM
        print(f"This is an {difficulty} exercise.")
        result = func(*args, **kwargs)
        return result

    return wrapper


def hard_q(func):
    """Defines the question as hard, print for now."""
    def wrapper(*args, **kwargs):
        difficulty: _QDiff = _QDiff.HARD
        print(f"This is an {difficulty} exercise.")
        result = func(*args, **kwargs)
        return result

    return wrapper