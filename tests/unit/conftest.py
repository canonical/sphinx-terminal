import pytest
from sphinx_terminal import TerminalDirective
from typing_extensions import override


class FakeTerminalDirective(TerminalDirective):
    @override
    def __init__(self, options, content):
        self.options = options
        self.content = content


@pytest.fixture
def fake_terminal_directive(request: pytest.FixtureRequest) -> FakeTerminalDirective:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeTerminalDirective(
        options=overrides.get("options", {}),
        content=overrides.get("content"),
    )
