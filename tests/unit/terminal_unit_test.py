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
from docutils import nodes
from sphinx import addnodes
from sphinx_terminal.directive import TerminalDirective
from typing_extensions import override

TERMINAL_CONTENT = """\

hello
"""


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


@pytest.mark.parametrize(
    "fake_terminal_directive",
    [{"options": {"input": "echo 'hello'"}, "content": [TERMINAL_CONTENT]}],
    indirect=True,
)
def test_terminal_directive(fake_terminal_directive: FakeTerminalDirective):
    expected = nodes.container()
    expected["classes"] = "terminal"

    highlight = addnodes.highlightlang()
    highlight["force"] = "False"
    highlight["lang"] = "text"
    highlight["linenothreshold"] = "10000"
    expected.append(highlight)

    input_container = nodes.container()
    input_container["classes"] = "input"

    prompt_container = nodes.container()
    prompt_container["classes"] = "prompt"
    prompt_text = nodes.literal(text="user@host:~$ ")
    prompt_container.append(prompt_text)
    input_container.append(prompt_container)

    command = nodes.literal(text="echo 'hello'")
    command["classes"] = "command"
    input_container.append(command)
    expected.append(input_container)

    output_block = nodes.literal_block(text="\nhello\n")
    output_block["classes"] = "terminal-code"
    output_block["xml:space"] = "preserve"
    expected.append(output_block)

    actual = fake_terminal_directive.run()[0]

    print(f"\n\n{str(expected)}\n\n")  # DELETE ME
    print(f"\n\n{str(actual)}\n\n")  # DELETE ME

    assert str(expected) == str(actual)


# Expected output

# <container classes="terminal copybutton scroll">
#   <highlightlang force="False" lang="text" linenothreshold="10000"/>

#   <container classes="input">
#     <container classes="prompt">
#       <literal>author@canonical:~/path$ </literal>
#     </container>
#     <literal classes="command">echo 'hello'</literal>
#   </container>

#   <literal_block classes="terminal-code" xml:space="preserve">
# hello
#   </literal_block>
