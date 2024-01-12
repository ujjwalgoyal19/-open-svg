"""Hello unit test module."""

from open_svg_tracing.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello open-svg-tracing"
