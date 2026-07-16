
Test doc
========

This document is parsed with bs4 to ensure that the rendered HTML matches the
expected output.

First, we test the user-host-dir syntax:

.. terminal::
    :copy:
    :scroll:
    :user: author
    :host: canonical
    :dir: ~/path

    input

    output

Then, the simpler prompt syntax:

.. terminal::
    :copy:
    :scroll:
    :prompt: PS C:\Users\JJ>

    I'm a PowerShell user now.

    Hooray.

The following documents include more examples for manual review:

.. toctree::
    :maxdepth: 1

    rst-examples
    myst-examples
