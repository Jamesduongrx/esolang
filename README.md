# esolang ![](https://github.com/jamesduongrx/esolang/workflows/tests/badge.svg)

A simple esolang for experimenting with different syntax and semantics of programming languages.

#Level 1:
```
    >>> interpreter.visit(parser.parse("if (0): { 20 } else 15"))
    15
    >>> interpreter.visit(parser.parse("if (1): { 25 } else 30"))
    25
    >>> interpreter.visit(parser.parse("a = 15; if (a): { 35 } else 40"))
    35
    >>> interpreter.visit(parser.parse("a = 0; if (a): { 50 } else 45"))
    45
    >>> interpreter.visit(parser.parse("a = 10; b = 5; if (a-b): { 60 } else 55"))
    60
    >>> interpreter.visit(parser.parse("a = 10; b = 10; if (a-b): { 70 } else 65"))
    65
    >>> interpreter.visit(parser.parse("x = 5; { x = x * 2; x + 10 }"))
    20
    '''
```
# Level 2:
```

    >>> interpreter.visit(parser.parse("a=0; for i in range(6+4) {a = a + i}"))
    55
    >>> interpreter.visit(parser.parse("n = 5; a = 0; for i in range(n) {a = a + i}; a"))
    10
    >>> interpreter.visit(parser.parse("n = 5; a = 0; for i in range(n) {n = n + 1; a = a + i}; a"))
    10
    >>> interpreter.visit(parser.parse("a = 0; for i in range(4) {for j in range(i + 2) {a = a + j}}; a"))
    16
    >>> interpreter.visit(parser.parse("1 > 0"))
    0
    >>> interpreter.visit(parser.parse("0 > 1"))
    1
    >>> interpreter.visit(parser.parse("a = 8; b = 4; (a - 3) > b"))
    True
    >>> interpreter.visit(parser.parse("a=0; while a < 15 {a = a + 2}; a"))
    16
    >>> interpreter.visit(parser.parse("a=0; n=3; while a + n < 12 {a = a + 2}; a"))
    6
    >>> interpreter.visit(parser.parse("a=2; while a < 8 {a = a * 3}; a"))
    18
```
# Level 3 

```
        >>> interpreter = Interpreter()
        >>> interpreter.visit(parser.parse("is_prime(1)"))
        False
        >>> interpreter.visit(parser.parse("is_prime(2)"))
        True
        >>> interpreter.visit(parser.parse("is_prime(3)"))
        True
        >>> interpreter.visit(parser.parse("is_prime(4)"))
        False
 ```
