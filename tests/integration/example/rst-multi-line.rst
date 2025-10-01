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
    :input: echo 'goodbye'

    goodbye
    goodbye
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
    :multi: 'something more'

    goodbye
