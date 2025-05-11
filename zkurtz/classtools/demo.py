"""Demo for the constant class."""

from dataclasses import FrozenInstanceError

from pytest import raises

from zkurtz.classtools.constantclass import constant


class Base:
    """Base class for demonstration."""

    @property
    def greetings(self) -> str:
        """Return a greeting message."""
        return "Hello, world!"


@constant
class MyPaths(Base):
    """Demo: A frozen class with constant values."""

    inputs = "input/path"
    outputs: str = "output/path"


def demo() -> None:
    """Demonstrate the use of the constant class."""

    print("MyPaths is a frozen class instance with the following values:")
    for name, value in MyPaths:
        print(f"    MyPaths.{name} = {value}")

    # __iter__ is defined in the class such that we can convert it directly to a dict:
    assert dict(MyPaths) == {
        "inputs": "input/path",
        "outputs": "output/path",
    }

    # The class inherited from the "Base" class with a greetings property:
    assert MyPaths.greetings == "Hello, world!"

    print("Item assignment like MyPaths.inputs = 'new/path' raises FrozenInstanceError")
    with raises(FrozenInstanceError):
        MyPaths.inputs = "new/path"  # pyright: ignore[reportAttributeAccessIssue]

    print("The class is already instantiated, so we can't call it (assuming no `__call__` method was defined)")
    assert isinstance(MyPaths, object)
    with raises(TypeError):
        MyPaths()  # pyright: ignore[reportCallIssue]


if __name__ == "__main__":
    demo()
