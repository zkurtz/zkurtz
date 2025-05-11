"""Using a dataclass as a python constant.

For when you want to wrap constants in a class in a way that leverages static type checking, but when you'd rather NOT
- use an extra "value" suffix every time you want to access a value, like you do with enums: `Enum.ITEM.value`
- have to instantiate the class to invoke frozen-ness, like you do with a frozen dataclass.
- use quoted keys to access values, like you do with a dict or TypedDict.
"""

from dataclasses import dataclass