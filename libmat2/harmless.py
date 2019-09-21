import shutil
from typing import Dict, Union
from . import abstract


class HarmlessParser(abstract.AbstractParser):
    """ This is the parser for filetypes that can not contain metadata. """
    mimetypes = {'text/plain', 'image/x-ms-bmp'}

    def get_meta(self) -> Dict[str, Union[str, dict]]:
        return dict()

    def remove_all(self, inplace:bool = False) -> bool:
        if not inplace:
            shutil.copy(self.filename, self.backup)
        return True
