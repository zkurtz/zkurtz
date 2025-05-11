from attr.exceptions import FrozenInstanceError
from pytest import raises

from zkurtz.classtools.demo import MyPaths, Simple


def test_constant() -> None:
    """Demonstrate the use of the constant class."""

    with raises(TypeError):
        MyPaths()  # pyright: ignore[reportCallIssue]

    with raises(FrozenInstanceError):
        MyPaths.inputs = "new/path"  # pyright: ignore[reportAttributeAccessIssue]

    # The class inherited from the "Base" class with a greetings property:
    assert MyPaths.greetings == "Hello, world!"

    # __iter__ is defined in the class such that we can convert it directly to a dict:
    assert dict(MyPaths) == {
        "inputs": "input/path",
        "outputs": "output/path",
    }

    print("A simple `frozen_instance` class is not iterable")
    with raises(TypeError):
        dict(Simple)
