"""Tests of asynchronous tasks."""


def test_byeworld_async(byeworld):
    """Test of ByWorld asynchronous task method."""
    task = byeworld.asynchronous.delay('test')
    assert task.get(timeout=10) == {'async': 'test'}
