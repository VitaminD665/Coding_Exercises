"""
Handle and encapsulate some of the logic for mngmt

"""
import inspect


class MemberCountingMeta(type):
    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        cls._refresh()
        return cls

    def __setattr__(cls, name, value) -> None:
        super().__setattr__(name, value)
        cls._refresh()

    def __delattr__(cls, name) -> None:
        super().__delattr__(name)
        cls._refresh()

    def _refresh(cls) -> None:
        exclude = {"__repr__"}
        methods = [
            n for n, v in cls.__dict__.items()
            if (inspect.isfunction(v) or isinstance(v, (staticmethod, classmethod)))
            and not n.startswith('_')
            and n not in exclude
        ]
        type.__setattr__(cls, "list_questions", sorted(methods))
        type.__setattr__(cls, "num_questions", len(methods))

    def __repr__(cls) -> str:
        return (
            f"{cls.__name__}("
            f"num_questions={getattr(cls, 'num_questions', 0)}/"
            f"{getattr(cls, 'count_neetcode', '?')}, "
            f"list={getattr(cls, 'list_questions', [])})")