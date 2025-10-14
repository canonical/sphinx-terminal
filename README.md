# sphinx-terminal

sphinx-terminal allows you to display terminal input and output in your Sphinx
documentation.

## Basic usage

To display terminal input and output in your rST document, use the `terminal` directive,
providing input and output as follows:

```
.. terminal::

    input

    output
```

Multiple input lines can be used, as long as they are in the same paragraph.
They will automatically be indented in the HTML output.

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

To enable a copy button for users, include the `:copy:` flag as a directive option.
Only the input will be available to copy.

```
.. terminal::
    :copy:

    echo 'hello'

    hello
```

Similarly, to make the output scrollable, include the `:scroll:` flag as a directive option.

```
.. terminal::
    :scroll:

    echo 'hello'

    hello
```

### No input command

Use the `:noinput:` option to prevent any text from being interpreted as a command input:

```
.. terminal::
    :noinput:

    output
```

### Copybutton support

When used in combination with [sphinx-copybutton](https://github.com/executablebooks/sphinx-copybutton)
ensure that `sphinx_copybutton` is higher in the `extensions` list than
`sphinx_terminal`.

## Project setup

sphinx-terminal is published on PyPI and can be installed with:

```bash
pip install sphinx-terminal
```

After adding sphinx-terminal to your Python project, update your Sphinx's conf.py file
to include sphinx-terminal as one of its extensions:

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
