import sys
import argparse
from lexer import tokenize
from aahaan_parser import parse
from interpreter import run_program

VERSION = "1.0.0"

def main():
    parser = argparse.ArgumentParser(description="Aahaan Language CLI")
    parser.add_argument("file", nargs="?", help="Path to .ahn file")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--debug", action="store_true", help="Show tokens and AST")
    
    args = parser.parse_args()

    if args.version:
        print(f"Aahaan Language v{VERSION}")
        return

    if not args.file:
        parser.print_help()
        return

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        return

    tokens = tokenize(code)
    if args.debug:
        print("Tokens:")
        for t in tokens:
            print(t)
        print("\nAST:")
    ast = parse(tokens)
    if args.debug:
        from pprint import pprint
        pprint(ast)
    print()
    run_program(ast)

if __name__ == "__main__":
    main()
