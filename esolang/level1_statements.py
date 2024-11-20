import lark
import esolang.level0_arithmetic


grammar = esolang.level0_arithmetic.grammar + r"""
    %extend start: start (";" start)*
        | assign_var
        | block
        | if_statement
        | /#.*/                -> comment

    if_statement: "if" condition ":" start "else" start

    ?condition: start

    block: "{" start* "}"

    assign_var: NAME "=" start

    NAME: /[_a-zA-Z][_a-zA-Z0-9]*/

    %extend atom: NAME -> access_var
"""
parser = lark.Lark(grammar)



class Interpreter(esolang.level0_arithmetic.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("a = 2"))
    2
    >>> interpreter.visit(parser.parse("a + 2"))
    4
    >>> interpreter.visit(parser.parse("a = a + 3"))
    5
    >>> interpreter.visit(parser.parse("b = 3"))
    3
    >>> interpreter.visit(parser.parse("a * b"))
    15
    >>> interpreter.visit(parser.parse("a = 3; {a+5}"))
    8
    >>> interpreter.visit(parser.parse("a = 3; {a=5; a+5}"))
    10
    >>> interpreter.visit(parser.parse("a = 3; {a=5}; a+5"))
    10
    >>> interpreter.visit(parser.parse("a = 3; {c=5}; c+5")) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: Variable c undefined

    >>> interpreter.visit(parser.parse("if (0): { 10 } else 5"))
    5
    >>> interpreter.visit(parser.parse("if (1): { 10 } else 5"))
    10
    >>> interpreter.visit(parser.parse("a = 10; if (a): { 10 } else 0"))
    10
    >>> interpreter.visit(parser.parse("a = 1; if (a): { 10 } else 100"))
    10
    >>> interpreter.visit(parser.parse("a = 2; b = 1; if (a-b): { 5 } else 1"))
    5
    >>> interpreter.visit(parser.parse("a = 2; b = 2; if (a-b): { 5 } else 1"))
    1
    >>> interpreter.visit(parser.parse("x = 2; { x = x + 3; x + 5 }"))
    10
    '''
    def __init__(self):
        self.stack = [{}]

    def _get_from_stack(self, name):
        for d in reversed(self.stack):
            if name in d:
                return d[name]
        raise ValueError(f"Variable {name} undefined")

    def _assign_to_stack(self, name, value):
        for d in reversed(self.stack):
            if name in d:
                d[name] = value
                return value
        self.stack[-1][name] = value
        return value

    def assign_var(self, tree):
        name = tree.children[0].value
        value = self.visit(tree.children[1])
        self._assign_to_stack(name, value)
        return value

    def access_var(self, tree):
        name = tree.children[0].value
        return self._get_from_stack(name)

    def block(self, tree):
        self.stack.append({})  
        result = None          
        for signal in tree.children:  
            result = self.visit(signal)
        self.stack.pop()  
        return result
    def if_statement(self, tree):
        condition_value = self.visit(tree.children[0])
        if condition_value:
            return self.visit(tree.children[1])
        else:
            return self.visit(tree.children[2])

