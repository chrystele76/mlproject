from mlproject.distance import haversine


def test_distance_right():
    assert type(haversine(31,40,50,38)) != 0
