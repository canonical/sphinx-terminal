# sphinx-terminal

<!-- Answer elevator-pitch questions about the extension – What is it? What does it do? What
essential problem does it solve? -->

sphinx-terminal allows you to display terminal input and output in your Sphinx
documentation.

## Basic usage

To display terminal input and output in your rST document, use the `terminal` directive,
providing input and output as follows:

```
.. terminal::
    :input: echo hello

        hello
```

To enable a copy button for users, include the `:copy:` flag as a directive option:

```
.. terminal::
    :copy:
    :input: echo hello

        hello
```

## Project setup

<!-- Provide the simplest way to install the extension. In most cases, this will
be via `pip`. -->

sphinx-terminal is published on PyPI and can be installed with:

```bash
pip install sphinx-terminal
```

After adding sphinx-terminal to your Python project, update your Sphinx's conf.py file
to include hello-ext as one of its extensions:

```python
extensions = [
    "sphinx_terminal"
]
```

## Community and support

You can report any issues or bugs on the project's [GitHub
repository](https://github.com/canonical/sphinx-terminal).

hello-ext is covered by the [Ubuntu Code of
Conduct](https://ubuntu.com/community/ethos/code-of-conduct).

## License and copyright

sphinx-terminal is released under the [GPL-3.0 license](LICENSE).

© 2025 Canonical Ltd.
