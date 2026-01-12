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

import importlib.util

from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx
from .directive import TerminalDirective
from sphinx_terminal import common

try:
    from ._version import __version__
except ImportError:
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("sphinx_terminal")
    except PackageNotFoundError:
        __version__ = "dev"


def setup(app: Sphinx) -> ExtensionMetadata:
    """Connect the extension to the Sphinx application instance.

    app (Sphinx): The Sphinx application instance.

    returns: ExtensionMetadata
    """
    # add sphinx-copybutton to Sphinx's extensions
    try:
        if importlib.util.find_spec("sphinx_copybutton") is not None:
            app.setup_extension("sphinx_copybutton")
    except ModuleNotFoundError:
        print("Could not find 'sphinx-copybutton'.")

    app.add_directive("terminal", TerminalDirective)
    common.add_css(app, "terminal.css")

    if app.config.copybutton_selector == "div.highlight pre":
        app.config.copybutton_selector = "span.copybutton, div:not(.terminal-code, .no-copybutton) > div.highlight > pre"

    # Configure copybutton to ignore the multiline prompt. These values will be
    # overridden if included in conf.py
    app.config.copybutton_prompt_is_regexp = True
    if app.config.copybutton_prompt_text == "":
        app.config.copybutton_prompt_text = "> |"

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


__all__ = ["__version__", "setup"]
