class Node: pass

class Print(Node):       
    def __init__(self, expr): self.expr = expr
class VarAssign(Node):   
    def __init__(self, name, expr): self.name = name; self.expr = expr
class IfElse(Node):      
    def __init__(self, cond, ifb, elseb): self.condition, self.if_body, self.else_body = cond, ifb, elseb
class WhileLoop(Node):   
    def __init__(self, cond, body): self.condition, self.body = cond, body
class FunctionDef(Node): 
    def __init__(self, name, body): self.name, self.body = name, body
class FunctionCall(Node):
    def __init__(self, name, args=[]): self.name, self.args = name, args
class Return(Node):      
    def __init__(self, value): self.value = value
class Input(Node):       
    def __init__(self, prompt): self.prompt = prompt
class BinOp(Node):       
    def __init__(self, left, op, right): self.left, self.op, self.right = left, op, right
class Literal(Node):     
    def __init__(self, value): self.value = value
class Var(Node):         
    def __init__(self, name): self.name = name
class ExprStmt(Node):    
    def __init__(self, expr): self.expr = expr

def parse(tokens):
    pos = 0
    def current(): return tokens[pos] if pos < len(tokens) else ('EOF', '')

    def eat(expected_type=None):
        nonlocal pos
        tok = current()
        if expected_type and tok[0] != expected_type:
            raise RuntimeError(f"[ParseError] Expected {expected_type}, got {tok}")
        pos += 1
        return tok

    def parse_expr():
        return parse_binop_rhs(parse_term())

    def parse_binop_rhs(left):
        while current()[0] in {"OP", "AND", "OR", "NEQ"}:
            if current()[0] == "NEQ":
                op = eat("NEQ")[1]
            else:
                op = eat(current()[0])[1]
            right = parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term():
        tok = current()
        if tok[0] == "NOT":
            eat("NOT")
            operand = parse_term()
            return BinOp(Literal(True), 'not', operand)
        elif tok[0] == "NUMBER":
            return Literal(eat()[1])
        elif tok[0] == "STRING":
            return Literal(eat()[1])
        elif tok[0] == "ID":
            name = eat("ID")[1]
            if current()[0] == "LPAREN":
                eat("LPAREN")
                args = []
                if current()[0] != "RPAREN":
                    args.append(parse_expr())
                    while current()[0] == "COMMA":
                        eat("COMMA")
                        args.append(parse_expr())
                eat("RPAREN")
                return FunctionCall(name, args)
            return Var(name)
        elif tok[0] == "LPAREN":
            eat("LPAREN")
            expr = parse_expr()
            eat("RPAREN")
            return expr
        else:
            raise RuntimeError(f"Unexpected token: {tok}")

    def parse_stmt():
        tok = current()

        if tok[0] == "ennaachu":
            eat("ennaachu")
            expr = parse_expr()
            return Print(expr)

        elif tok[0] == "vechutten":
            eat("vechutten")
            name = eat("ID")[1]
            eat("OP")  # expect '='
            expr = parse_expr()
            return VarAssign(name, expr)

        elif tok[0] == "ID" and pos + 1 < len(tokens) and tokens[pos + 1][0] == "OP" and tokens[pos + 1][1] == "=":
            # assignment without `vechutten`
            name = eat("ID")[1]
            eat("OP")  # '='
            expr = parse_expr()
            return VarAssign(name, expr)

        elif tok[0] == "irundhaachu":
            eat("irundhaachu")
            eat("LPAREN")
            condition = parse_expr()
            eat("RPAREN")
            eat("LBRACE")
            if_body = []
            while current()[0] != "RBRACE":
                if_body.append(parse_stmt())
            eat("RBRACE")

            # 👇 Handle multiple 'illana irundhaachu' and final 'illana'
            else_body = []
            while current()[0] == "illana":
                eat("illana")
                if current()[0] == "irundhaachu":
                    # Handle 'else if'
                    nested = parse_stmt()
                    else_body = [nested]
                    break
                elif current()[0] == "LBRACE":
                    eat("LBRACE")
                    while current()[0] != "RBRACE":
                        else_body.append(parse_stmt())
                    eat("RBRACE")
                    break
                else:
                    raise RuntimeError(f"[ParseError] Expected 'irundhaachu' or '{{' after 'illana', got {current()}")

            return IfElse(condition, if_body, else_body)

        elif tok[0] == "vandhacha":
            eat("vandhacha")
            eat("LPAREN")
            condition = parse_expr()
            eat("RPAREN")
            eat("LBRACE")
            body = []
            while current()[0] != "RBRACE":
                body.append(parse_stmt())
            eat("RBRACE")
            return WhileLoop(condition, body)

        elif tok[0] == "kelu":
            eat("kelu")
            prompt = parse_expr()
            return Input(prompt)

        elif tok[0] == "odi":
            eat("odi")
            value = parse_expr()
            return Return(value)

        elif tok[0] == "kaatuda":
            eat("kaatuda")
            name = eat("ID")[1]
            eat("LPAREN")
            eat("RPAREN")
            eat("LBRACE")
            body = []
            while current()[0] != "RBRACE":
                body.append(parse_stmt())
            eat("RBRACE")
            return FunctionDef(name, body)

        elif tok[0] in ("ID", "NUMBER", "STRING", "LPAREN"):
            expr = parse_expr()
            return ExprStmt(expr)

        else:
            raise RuntimeError(f"[ParseError] Unknown statement start: {tok}")

    stmts = []
    while current()[0] != "EOF":
        stmts.append(parse_stmt())
    return stmts
