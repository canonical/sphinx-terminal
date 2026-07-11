# MyST examples

## Multi-line input

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path

input line 1
input line 2

output line 1
output line 2
output line 3
```

## No input

```{terminal}
:user: author
:host: canonical
:dir: ~/path
:output-only:

output line 1
output line 2

output line 3
```

## No output

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path

input line 1
input line 2
input line 3
```

## Stacked terminals

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path

input 1

output 1
```

```{terminal}
:copy:
:user: author
:host: canonical
:dir: ~/path

input 2

output 2
```

## Code blocks

```{code-block}
This should remain copyable.
```

```{code-block} text
:class: no-copybutton

This shouldn't be copyable.
```
