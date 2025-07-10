from aahaan_parser import *

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

def eval_expr(expr, env):
    if isinstance(expr, Literal):
        return expr.value

    elif isinstance(expr, Var):
        val = env.get(expr.name)
        if val is None:
            raise RuntimeError(f"[RuntimeError] Variable '{expr.name}' is not defined.")
        return val

    elif isinstance(expr, BinOp):
        left = eval_expr(expr.left, env)
        right = eval_expr(expr.right, env)
        op = expr.op

        try:
            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif op == '-': return left - right
            elif op == '*': return left * right
            elif op == '/': return left / right
            elif op == '%': return left % right
            elif op == '>': return left > right
            elif op == '<': return left < right
            elif op == '>=': return left >= right
            elif op == '<=': return left <= right
            elif op == '==': return left == right
            elif op == '!=': return left != right
            elif op == 'and': return left and right
            elif op == 'or': return left or right
            elif op == 'not': return not right
            else:
                raise RuntimeError(f"[RuntimeError] Unknown operator '{op}'")
        except Exception as e:
            raise RuntimeError(f"[RuntimeError] Operation '{op}' failed: {e}")

    elif isinstance(expr, FunctionCall):
        fn = env["functions"].get(expr.name)
        args = [eval_expr(arg, env) for arg in expr.args]

        if not fn:
            if expr.name == "max": return max(*args)
            if expr.name == "min": return min(*args)
            if expr.name == "pow": return pow(*args)
            raise RuntimeError(f"[RuntimeError] Function '{expr.name}' not found.")

        local_env = env.copy()
        for stmt in fn.body:
            try:
                run_stmt(stmt, local_env)
            except ReturnSignal as rs:
                return rs.value
        return None

    else:
        raise RuntimeError(f"[RuntimeError] Unknown expression type: {type(expr)}")

def run_stmt(stmt, env):
    if isinstance(stmt, Print):
        print(eval_expr(stmt.expr, env))

    elif isinstance(stmt, VarAssign):
        env[stmt.name] = eval_expr(stmt.expr, env)

    elif isinstance(stmt, FunctionDef):
        env["functions"][stmt.name] = stmt

    elif isinstance(stmt, Return):
        raise ReturnSignal(eval_expr(stmt.value, env))

    elif isinstance(stmt, Input):
        val = input(eval_expr(stmt.prompt, env))
        try:
            val = int(val)
        except:
            try:
                val = float(val)
            except:
                pass
        env["_"] = val

    elif isinstance(stmt, IfElse):
        cond = eval_expr(stmt.condition, env)
        if cond:
            for s in stmt.if_body:
                run_stmt(s, env)
        else:
            for s in stmt.else_body:
                run_stmt(s, env)

    elif isinstance(stmt, WhileLoop):
        while eval_expr(stmt.condition, env):
            for s in stmt.body:
                run_stmt(s, env)

    elif isinstance(stmt, ExprStmt):
        eval_expr(stmt.expr, env)

def run_program(ast):
    env = {}
    env["functions"] = {}
    for stmt in ast:
        run_stmt(stmt, env)
