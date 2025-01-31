from typing import Self, Type, Union

from anymethod import anymethod


class A:
    @anymethod
    def whoami(owner) -> Union[Self, Type[Self]]:
        return owner


def test_typing() -> None:
    assert A.whoami() is A
