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
    goodbye
    goodbye

What is happening?
Why is the line above me not there?

The entire paragraph is getting eaten... Hmm.

Why?

.. terminal::
    :copy:
    :scroll:
    :user: author
    :host: canonical
    :dir: ~/path
    :input: echo 'hello'
    :multi: 3

    echo 'more'

    echo 'even more!'

    hello

    :input: echo 'goodbye'
    :multi: 'something more'

    goodbye

.. why

I'm very confused.
