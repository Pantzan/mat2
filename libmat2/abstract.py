import abc
import os
import re
from typing import Set, Dict, Union

assert Set  # make pyflakes happy


class AbstractParser(abc.ABC):
    """ This is the base class of every parser.
    It might yield `ValueError` on instantiation on invalid files,
    and `RuntimeError` when something went wrong in `remove_all`.
    """
    meta_list = set()  # type: Set[str]
    mimetypes = set()  # type: Set[str]
    suffix = '.original'

    def __init__(self, filename: str) -> None:
        """
        :raises ValueError: Raised upon an invalid file
        """
        if re.search('^[a-z0-9./]', filename) is None:
            # Some parsers are calling external binaries,
            # this prevents shell command injections
            filename = os.path.join('.', filename)

        self.filename = filename
        self.output_filename = filename

        self.lightweight_cleaning = False

    @abc.abstractmethod
    def get_meta(self) -> Dict[str, Union[str, dict]]:
        """Return all the metadata of the current file"""

    def remove_all(self) -> bool:
        """
        Remove all the metadata of the current file

        :raises RuntimeError: Raised if the cleaning process went wrong.
        """
        self.output_filename = self.filename
        self.filename = self.filename + self.suffix
        os.rename(filename, filename + self.suffix)
