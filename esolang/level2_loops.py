import lark
import esolang.level1_statements


grammar = esolang.level1_statements.grammar + r"""
    %extend start: forloop 
                | whileloop
                | comparison
                | range 

    forloop: "for" NAME "in" range block

    range: "range" "(" start ")"

    comparison: start COMPARISON_OPERATOR start

    COMPARISON_OPERATOR: ">" | "<" | ">=" | "<=" | "==" | "!="

    whileloop: "while" comparison block


"""
parser = lark.Lark(grammar)


class Interpreter(esolang.level1_statements.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("for i in range(10) {i}"))
    9
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; a"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; i")) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: Variable i undefined

    >>> interpreter.visit(parser.parse("a=5; for i in range(a) {a = a + i}; a"))
    15
    >>> interpreter.visit(parser.parse("a=0; while a < 10 {a = a + 1}"))
    10
    >>> interpreter.visit(parser.parse("a=0; while a < 5 {a = a + 1}; a"))
    5
    >>> interpreter.visit(parser.parse("1 > 0"))
    True
    >>> interpreter.visit(parser.parse("0 > 1"))
    False
    >>> interpreter.visit(parser.parse("a=0; while a < 6 {a = a + 1}; a"))
    6
    >>> interpreter.visit(parser.parse("a=0; while a < 7 {a = a + 3}; a"))
    9
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
    '''
    def range(self, tree):
        if len(tree.children) == 1:
            stop = self.visit(tree.children[0])
            return range(0, stop)

        start = self.visit(tree.children[0])
        stop = self.visit(tree.children[1])
        return range(start, stop)


    def forloop(self, tree):
        varname = tree.children[0].value
        loop_range = self.visit(tree.children[1])
        block = tree.children[2]

        self.stack.append({})
        result = None

        for value in loop_range:
            self.stack[-1][varname] = value  
            result = self.visit(block) 
        self.stack.pop()
        return result

    def whileloop(self, tree):
        result = None
        while self.visit(tree.children[0]):
            result = self.visit(tree.children[1])
        return result


    def comparison(self, tree):
        v1 = self.visit(tree.children[0]) 
        op = tree.children[1].value      
        v2 = self.visit(tree.children[2])  
        if op == ">":
            return v1 > v2
        elif op == "<":
            return v1 < v2
        elif op == ">=":
            return v1 >= v2
        elif op == "<=":
            return v1 <= v2
        elif op == "==":
            return v1 == v2
        elif op == "!=":
            return v1 != v2


            



