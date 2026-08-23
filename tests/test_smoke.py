from dailies.cli import main


def test_entrypoint_is_callable() -> None:
    assert callable(main)
