import lark
import esolang.level1_statements


grammar = esolang.level1_statements.grammar + r"""
    %extend start: forloop 
                | whileloop

    forloop: "for" NAME "in" range block

    range: "range" "(" start ")"

    whileloop: "while" comparison block
    
    comparison: start "<" start
              | start ">" start
              | start "<=" start
              | start ">=" start
              | start "==" start
              | start "!=" start


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
        x = tree.children[0]
        y = tree.children[1]
        self.stack.append({})
        while self.visit(x):
            self.visit(y)
        self.stack.pop()

    def comparison(self, tree):
        left = self.visit(tree.children[0])
        operator = tree.children[1].value
        right = self.visit(tree.children[2])
        if operator == "<": return left < right
        if operator == "<=": return left <= right
        if operator == ">": return left > right
        if operator == ">=": return left >= right
        if operator == "==": return left == right
        if operator == "!=": return left != right
        
        raise ValueError(f"Unknown operator resulted in: {operator}")



