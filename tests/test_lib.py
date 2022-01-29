from mlproject.lib import hello_world
from mlproject.lib import week_end


def test_length_of_hello_world():
    assert len(hello_world()) != 0


def test_length_of_week_end():
    assert len(week_end()) != 0
