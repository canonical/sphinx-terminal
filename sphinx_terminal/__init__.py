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

"""Adds the directive to Sphinx."""

from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx
from .directive import TerminalDirective
from sphinx_terminal import common

try:
    from ._version import __version__
except ImportError:
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("pydantic_kitbash")
    except PackageNotFoundError:
        __version__ = "dev"


def setup(app: Sphinx) -> ExtensionMetadata:
    """Connect the extension to the Sphinx application instance.

    app (Sphinx):

    returns: ExtensionMetadata
    """
    app.add_directive("terminal", TerminalDirective)
    common.add_css(app, "terminal.css")

    copybutton_classes = "div.terminal.copybutton > div.container > code.command, div:not(.terminal-code, .no-copybutton) > div.highlight > pre"
    if "copybutton_selector" not in app.config.values:
        app.add_config_value("copybutton_selector", copybutton_classes, "env")
    if app.config.copybutton_selector == "div.highlight pre":
        app.config.copybutton_selector = copybutton_classes

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


__all__ = ["__version__", "setup"]
