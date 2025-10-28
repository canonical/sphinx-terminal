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

"""The core elements of the sphinx-terminal directive."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective


class TerminalDirective(SphinxDirective):
    """Define the terminal directive's state and behavior."""

    required_arguments = 0
    optional_arguments = 0
    has_content = True
    option_spec = {
        "class": directives.class_option,
        "user": directives.unchanged,
        "host": directives.unchanged,
        "dir": directives.unchanged,
        "output-only": directives.flag,
        "scroll": directives.flag,
        "copy": directives.flag,
    }

    @staticmethod
    def input_line(
        prompt_text: str,
        commands: list[str],
        *,
        is_copyable: bool,
    ) -> nodes.container:
        """Construct the prompt with the user-provided options (if any)."""
        input_line = nodes.container()
        input_line["classes"].append("input")

        # To let the prompt be styled separately in LaTeX, it needs to be
        # wrapped in a container. This adds an extra div to the HTML output,
        # but what's a few bytes between friends?
        prompt_container = nodes.container()
        prompt_container["classes"].append("prompt")

        prompt = nodes.literal(text=prompt_text)
        prompt_container.append(prompt)
        input_line.append(prompt_container)

        command = nodes.inline()

        for line in commands:
            command.append(nodes.literal(text=f"{line}\n"))

        command["classes"].append("command")
        if is_copyable:
            command["classes"].append("copybutton")

        input_line.append(command)
        return input_line

    def run(self) -> list[nodes.Node]:
        """Construct the output of the terminal directive."""
        # if :user: or :host: are provided, replace those in the prompt
        classes = self.options.get("class", "")
        user = self.options.get("user", "user")
        host = self.options.get("host", "host")
        prompt_dir = self.options.get("dir", "~")
        user_symbol = "#" if user == "root" else "$"
        has_input = "output-only" not in self.options

        if user and host:
            prompt_text = f"{user}@{host}:{prompt_dir}{user_symbol} "
        elif user and not host:
            # Only the user is supplied
            prompt_text = f"{user}:{prompt_dir}{user_symbol} "
        else:
            # Omit both user and host, just showing the host
            # doesn't really make sense
            prompt_text = f"{prompt_dir}{user_symbol} "

        out = nodes.container()
        out["classes"].append("terminal")
        for item in classes:
            out["classes"].append(item)
        if "scroll" in self.options:
            out["classes"].append("scroll")

        # The super-large value for linenothreshold is a major hack since I
        # can't figure out how to disable line numbering and the
        # linenothreshold kwarg seems to be required.
        out.append(
            addnodes.highlightlang(lang="text", force=False, linenothreshold=10000)
        )

        # Split inputs and output
        input_lines: list[str] = []
        output_lines: list[str] = []

        # Add the prompt and input
        for line in self.content:
            if has_input:
                if has_input := bool(line.strip()):
                    input_lines += [line]
            else:
                output_lines += [line]

        if input_lines:
            out.append(
                self.input_line(
                    prompt_text,
                    [input_lines[0]] + ["> " + line for line in input_lines[1:]],
                    is_copyable="copy" in self.options,
                )
            )

        # Add output lines
        if output_lines:
            output = nodes.literal_block(text="\n".join(output_lines))
            output["classes"].append("terminal-code")
            out.append(output)

        return [out]
