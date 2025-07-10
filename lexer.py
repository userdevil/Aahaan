import re

TOKEN_SPEC = [
    ("NUMBER",     r'\d+'),
    ("STRING",     r'"[^"]*"'),
    ("NEQ",        r'!='),              # != operator
    ("OP", r'==|!=|<=|>=|[+\-*/%><=]'),
    ("AND",        r'and'),
    ("OR",         r'or'),
    ("NOT",        r'not'),
    ("ID",         r'[a-zA-Z_]\w*'),
    ("LPAREN",     r'\('),
    ("RPAREN",     r'\)'),
    ("LBRACE",     r'\{'),
    ("RBRACE",     r'\}'),
    ("COMMA",      r','),
    ("NEWLINE",    r'\n'),
    ("SKIP",       r'[ \t]+'),
    ("MISMATCH",   r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

KEYWORDS = {
    "vechutten", "ennaachu", "irundhaachu", "illana",
    "vandhacha", "kaatuda", "odi", "kelu"
}

def tokenize(code):
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == "NUMBER":
            tokens.append(("NUMBER", int(value)))
        elif kind == "STRING":
            tokens.append(("STRING", value.strip('"')))
        elif kind == "ID":
            if value in KEYWORDS:
                tokens.append((value, value))
            else:
                tokens.append(("ID", value))
        elif kind in {"OP", "AND", "OR", "NOT", "NEQ"}:
            tokens.append((kind, value))
        elif kind in {"LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA"}:
            tokens.append((kind, value))
        elif kind == "NEWLINE" or kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character: {value}")
    return tokens
