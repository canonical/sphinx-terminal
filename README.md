# sphinx-terminal

sphinx-terminal allows you to display terminal input and output in your Sphinx
documentation.

## Basic usage

To display terminal input and output in your Sphinx document, use the `terminal`
directive, providing input and output as follows:

```
.. terminal::

    input

    output
```

Input can span multiple lines, as long as the lines are in the same paragraph.
Everything after the first blank line is rendered as output.

The prompt defaults to `user@host:~$`. To customize this, use the `:user:`, `:host:`,
and `:dir:` options.

```
.. terminal::
    :user: author
    :host: canonical
    :dir: ~/path

    echo 'hello'

    hello
```

To render only the output of a command, include the `:output-only:` flag in the
directive's options.

```
.. terminal::
    :output-only:

    This is rendered as output.
```

To enable a copy button for users, include the `:copy:` flag as a directive option.
Only the input can be copied.

```
.. terminal::
    :copy:

    echo 'hello'

    hello
```

Similarly, to make the output scrollable, include the `:scroll:` flag as a directive
option.

```
.. terminal::
    :scroll:

    echo 'hello'

    hello
```

## Project setup

sphinx-terminal is published on PyPI and can be installed with:

```bash
pip install sphinx-terminal
```

After adding sphinx-terminal to your Python project, update Sphinx's conf.py file to
include sphinx-terminal as one of its extensions:

```python
extensions = [
    "sphinx_terminal"
]
```

## Community and support

You can report any issues or bugs on the project's [GitHub
repository](https://github.com/canonical/sphinx-terminal).

If you're interested in contributing, start with the [contribution
guide](https://github.com/canonical/sphinx-terminal/blob/main/CONTRIBUTING.md).

sphinx-terminal is covered by the [Ubuntu Code of
Conduct](https://ubuntu.com/community/ethos/code-of-conduct).

## License and copyright

sphinx-terminal is released under the [GPL-3.0 license](LICENSE).

© 2025 Canonical Ltd.
