import re
from typing import List, Union


class DialogFormatter:
    def __init__(self, replacer: Union[str, List[str, str]]):
        if isinstance(replacer, str):
            self.replacers: List[str, str] = [replacer, replacer]
        elif isinstance(replacer, list):
            self.replacers = replacer

    def format(self, text: str, **attrs) -> str:
        result: text = text
        for key, value in attrs.items():
            re.compile("{0}{key}{1}".format(*self.replacers, key=key)).match(text)
        return result
