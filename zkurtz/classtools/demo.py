"""Demo for the constant class."""

from dataclasses import FrozenInstanceError

from pytest import raises

from zkurtz.classtools.constantclass import constant


@constant
class MyPaths:
    """Demo: A frozen class with constant values."""

    inputs = "input/path"
    outputs: str = "output/path"


def demo() -> None:
    """Demonstrate the use of the constant class."""

    print("MyPaths is a frozen class instance with the following values:")
    for name, value in MyPaths:
        print(f"    MyPaths.{name} = {value}")

    print("Item assignment like MyPaths.inputs = 'new/path' raises FrozenInstanceError")
    with raises(FrozenInstanceError):
        MyPaths.inputs = "new/path"  # pyright: ignore[reportAttributeAccessIssue]

    print("The class is already instantiated, so we can't call it (assuming no `__call__` method was defined)")
    assert isinstance(MyPaths, object)
    with raises(TypeError):
        MyPaths()  # pyright: ignore[reportCallIssue]


if __name__ == "__main__":
    demo()
