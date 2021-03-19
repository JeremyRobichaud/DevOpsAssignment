from src.Car import Direction

direction_schema = {
    "FORWARD": {
        "value": 1,
        "name": "FORWARD"
    },
    "REVERSE": {
        "value": 2,
        "name": "REVERSE"
    },
    "STOPPED": {
        "value": 3,
        "name": "STOPPED"
    }

}


def test_forward():
    # This test is to make sure the Direction ENUM follows it's schema
    forward = Direction.FORWARD
    assert forward.value == direction_schema["FORWARD"]["value"]
    assert forward.name == direction_schema["FORWARD"]["name"]


def test_reverse():
    # This test is to make sure the Direction ENUM follows it's schema
    reverse = Direction.REVERSE
    assert reverse.value == direction_schema["REVERSE"]["value"]
    assert reverse.name == direction_schema["REVERSE"]["name"]


def test_stopped():
    # This test is to make sure the Direction ENUM follows it's schema
    stopped = Direction.STOPPED
    assert stopped.value == direction_schema["STOPPED"]["value"]
    assert stopped.name == direction_schema["STOPPED"]["name"]

