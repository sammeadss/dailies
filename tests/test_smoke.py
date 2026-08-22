from dailies.cli import main


def test_trivial() -> None:
    assert callable(main)
