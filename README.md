![tests](https://github.com/Jamesduongrx/esolang/workflows/tests/badge.svg?cache=0)

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
    >>> interpreter.visit(parser.parse("a=5; for i in range(a) {a = a + i}; a"))
    15
    >>> interpreter.visit(parser.parse("1 > 0"))
    True
    >>> interpreter.visit(parser.parse("0 > 1"))
    False
    >>> interpreter.visit(parser.parse("a=10; while a > 0 {a = a - 2}; a"))
    0
    >>> interpreter.visit(parser.parse("a=1; while a < 4 {a = a * 2}; a"))
    4
    >>> interpreter.visit(parser.parse("a=0; for i in range(3) {a = a + i}; a"))
    3
    >>> interpreter.visit(parser.parse("a=0; while a < 5 {a = a + 2}; a"))
    6  
    >>> interpreter.visit(parser.parse("a=0; while a < 10 {a = a + 3}; a"))
    12
    >>> interpreter.visit(parser.parse("a=5; while a > 3 {a = a - 1}; a"))
    3
    >>> interpreter.visit(parser.parse("a=0; while a < 2 {a = a + 1}; a"))
    2
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
