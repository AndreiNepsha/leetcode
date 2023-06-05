import pytest


@pytest.fixture
def factory():
    def _f(text):
        print("before yield")
        yield text
        print("after yield")

    return _f


@pytest.fixture
def obj(factory):
    yield from factory("text")


def test(obj):
    print("before obj")
    print(obj)
    print("after obj")
