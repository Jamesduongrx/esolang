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

    >>> interpreter.visit(parser.parse("a=0; for i in range(6+4) {a = a + i}"))
    55
    >>> interpreter.visit(parser.parse("n = 5; a = 0; for i in range(n) {a = a + i}; a"))
    10
    >>> interpreter.visit(parser.parse("n = 5; a = 0; for i in range(n) {n = n + 1; a = a + i}; a"))
    10
    >>> interpreter.visit(parser.parse("a = 0; for i in range(4) {for j in range(i + 2) {a = a + j}}; a"))
    16
    >>> interpreter.visit(parser.parse("1 > 0"))
    True
    >>> interpreter.visit(parser.parse("0 > 1"))
    False
    >>> interpreter.visit(parser.parse("a = 8; b = 4; (a - 3) > b"))
    True
    >>> interpreter.visit(parser.parse("a=0; while a < 15 {a = a + 2}; a"))
    16
    >>> interpreter.visit(parser.parse("a=0; n=3; while a + n < 12 {a = a + 2}; a"))
    6
    >>> interpreter.visit(parser.parse("a=2; while a < 8 {a = a * 3}; a"))
    18

    '''
    def range(self, tree):
        stop = self.visit(tree.children[0])  
        return range(0, stop)


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



            



