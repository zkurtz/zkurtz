from dataclasses import FrozenInstanceError

from pytest import raises

from zkurtz.classtools.demo import MyPaths


def demo() -> None:
    """Demonstrate the use of the constant class."""

    with raises(FrozenInstanceError):
        MyPaths.inputs = "new/path"  # pyright: ignore[reportAttributeAccessIssue]

    with raises(TypeError):
        MyPaths()  # pyright: ignore[reportCallIssue]

    breakpoint()
