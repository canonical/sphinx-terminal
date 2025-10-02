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

    :multi: echo 'something'
    :multi: echo 'something more'
    hello
    something
    something more

    :input: echo 'goodbye'
    goodbye

Best not to stack inputs:

.. terminal::
    :copy:
    :scroll:
    :user: author
    :host: canonical
    :dir: ~/path
    :input: echo 'hello'

    :multi: echo 'more'
    :multi: echo 'even more!'

    :input: echo 'goodbye'
    :multi: echo 'something more'
