import abc
import os
from typing import Set, Dict

assert Set  # make pyflakes happy


class AbstractParser(abc.ABC):
    """ This is the base class of every parser.
    It might yield `ValueError` on instantiation on invalid files.
    """
    meta_list = set()  # type: Set[str]
    mimetypes = set()  # type: Set[str]

    def __init__(self, filename: str, lightweight_cleaning: bool=False) -> None:
        """
        :raises ValueError: Raised upon an invalid file
        """
        self.filename = filename
        fname, extension = os.path.splitext(filename)
        self.output_filename = fname + '.cleaned' + extension
        self.lightweight_cleaning = lightweight_cleaning

    @abc.abstractmethod
    def get_meta(self) -> Dict[str, str]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def remove_all(self) -> bool:
        pass  # pragma: no cover
