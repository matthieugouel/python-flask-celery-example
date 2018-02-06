"""Tests of main asynchronous tasks."""


def test_byeworld_async(byeworld_asynchronous):
    """Test of ByWorld asynchronous task method."""
    assert byeworld_asynchronous.asynchronous('test') == {'async': 'test'}
