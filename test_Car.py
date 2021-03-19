from src.Car import Car, Direction


def test_creation():
    # This test is to make sure creating a car doesn't given an error and returns something
    car = Car()
    assert car
    assert car.direction == Direction.STOPPED


def test_moveForward_from_stop():
    # Car tests from STOPPED -> FORWARD #
    car = Car()
    car.stop()
    assert car.direction == Direction.STOPPED

    car.moveForward()
    assert car.direction == Direction.FORWARD


def test_moveForward_from_reverse():
    # Car tests from REVERSE -> FORWARD #
    car = Car()
    car.moveBackward()
    assert car.direction == Direction.REVERSE

    car.moveForward()
    assert car.direction == Direction.FORWARD


def test_moveBackward_from_stop():
    # Car tests from STOPPED -> REVERSE #
    car = Car()
    car.stop()
    assert car.direction == Direction.STOPPED

    car.moveBackward()
    assert car.direction == Direction.REVERSE


def test_moveBackward_from_forward():
    # Car tests from FORWARD -> REVERSE #
    car = Car()
    car.moveForward()
    assert car.direction == Direction.FORWARD

    car.moveBackward()
    assert car.direction == Direction.REVERSE


def test_stop_from_forward():
    # Car tests from FORWARD -> STOPPED #
    car = Car()
    car.moveForward()
    assert car.direction == Direction.FORWARD

    car.stop()
    assert car.direction == Direction.STOPPED


def test_stop_from_reverse():
    # Car tests from REVERSE -> STOPPED #
    car = Car()
    car.moveBackward()
    assert car.direction == Direction.REVERSE

    car.stop()
    assert car.direction == Direction.STOPPED


def test_isMoving_stop():
    # This test is to make sure isMoving is false when the car is stopped
    car = Car()
    car.stop()
    assert car.direction == Direction.STOPPED
    assert not car.isMoving()


def test_isMoving_forward():
    # This test is to make sure isMoving is true when the car is forward
    car = Car()
    car.moveForward()
    assert car.direction == Direction.FORWARD
    assert car.isMoving()


def test_isMoving_backward():
    # This test is to make sure isMoving is true when the car is backward
    car = Car()
    car.moveBackward()
    assert car.direction == Direction.REVERSE
    assert car.isMoving()

