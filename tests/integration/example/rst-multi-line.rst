RST multi line
==============

Initial multiline

.. terminal::
    :copy:
    :scroll:
    :user: author
    :host: canonical
    :dir: ~/path
    :input: echo 'hello'
    :multi: 2

    echo 'something'
    echo 'something more'

    hello
    :input: echo 'goodbye'

    goodbye

Content multiline

Why?

.. terminal::
    :copy:
    :scroll:
    :user: author
    :host: canonical
    :dir: ~/path
    :input: echo 'hello'

    hello

    :input: echo 'goodbye'
    :multi: 'something more'

    goodbye
