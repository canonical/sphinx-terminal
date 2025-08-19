# This file is part of sphinx-terminal.
#
# Copyright 2025 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License version 3, as published by the Free Software
# Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY
# QUALITY, or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from docutils.core import publish_doctree
from sphinx_terminal.directive import TerminalDirective
from typing_extensions import override


class FakeTerminalDirective(TerminalDirective):
    @override
    def __init__(self, arguments):
        self.arguments = arguments


@pytest.fixture
def fake_terminal_directive(request: pytest.FixtureRequest) -> FakeTerminalDirective:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeTerminalDirective(arguments=overrides.get("arguments", []))


@pytest.mark.parametrize(
    "fake_terminal_directive",
    [{"arguments": ["world"]}],
    indirect=True,
)
def test_hello_directive(fake_terminal_directive: FakeTerminalDirective):
    expected = ""
    actual = ""

    assert str(expected) == str(actual)
