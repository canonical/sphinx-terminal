# Myst multi line

Option based multiline

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path
:input: echo 'hello'
:multi: 2

echo 'more'
echo 'goodbye'

goodbye
```

Mid content multiline

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path
:input: echo 'hello'

hello

:input: echo 'goodbye'
:multi: echo 'more'
:multi: echo 'even more'

goodbye
```
