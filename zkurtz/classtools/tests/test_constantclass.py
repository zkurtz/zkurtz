from dataclasses import FrozenInstanceError

from pytest import raises

from zkurtz.classtools.demo import MyPaths


def test_constant() -> None:
    """Demonstrate the use of the constant class."""

    with raises(FrozenInstanceError):
        MyPaths.inputs = "new/path"  # pyright: ignore[reportAttributeAccessIssue]

    with raises(TypeError):
        MyPaths()  # pyright: ignore[reportCallIssue]

    # The class inherited from the "Base" class with a greetings property:
    assert MyPaths.greetings == "Hello, world!"

    # __iter__ is defined in the class such that we can convert it directly to a dict:
    assert dict(MyPaths) == {
        "inputs": "input/path",
        "outputs": "output/path",
    }
