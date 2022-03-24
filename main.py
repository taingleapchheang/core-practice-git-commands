import pytest


def always_returns_true(value):
    if bool(value) == True:
        return True


def test_always_returns_true():
    #Arrange
    value = 1

    #Act
    result = always_returns_true(value)

    #Assert
    assert bool(result) is True
