"""Using a dataclass as a python constant.

For when you want to wrap constants in a class in a way that leverages static type checking, but when you'd rather NOT
- use an extra "value" suffix every time you want to access a value, like you do with enums: `Enum.ITEM.value`
- have to instantiate the class to invoke frozen-ness, like you do with a frozen dataclass.
- use quoted keys to access values, like you do with a dict or TypedDict.

Illustrate the functionality in this module by running the demo:
    python -m zkurtz.classtools.demo
"""

from typing import Any, Callable, Iterator, Type

from attrs import fields, frozen


def _get_simple_attributes(cls: Type) -> list[str]:
    """Returns a list of simple attribute names.

    An attribute is considered "simple" if it is not a method or property that was defined within the scope of the
    class or a built-in magic attribute.
    """
    names = []
    for name, value in cls.__dict__.items():
        # Skip built-in magic attributes
        if name.startswith("__") and name.endswith("__"):
            continue
        # Skip functions defined using 'def' within the scope of the class or any parent class
        if isinstance(value, Callable):
            if any(value.__qualname__.startswith(base.__name__ + ".") for base in cls.__mro__):
                continue
        names.append(name)
    return names


def _iterator_over_fields(self: Any) -> Iterator[tuple[str, Any]]:
    """Iterate over the field names of the dataclass."""
    for field in fields(type(self)):
        yield field.name, field.default


def frozen_instance(cls: Any) -> Any:
    """Decorator to render a class declaration into into a frozen class instance."""
    for name in _get_simple_attributes(cls):
        if name in cls.__annotations__:
            continue
        value = getattr(cls, name)
        cls.__annotations__[name] = type(value)

    output_class = frozen(init=False)(cls)
    assert isinstance(output_class, Callable), "Expected class to be callable to allow instantiation"
    return output_class()


def iterable_frozen_instance(cls: Any) -> Any:
    """Decorator to render an iterable frozen instance."""
    cls.__iter__ = _iterator_over_fields
    return frozen_instance(cls)
