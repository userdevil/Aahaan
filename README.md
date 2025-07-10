# 🪔 Aahaan Programming Language

**Aahaan** is a fun, expressive, beginner-friendly programming language based on iconic **Tamil movie dialogues**. It brings the magic of Tamil cinema into the world of code by turning famous lines like `ennaachu`, `vechutten`, `irundhaachu`, and more into powerful programming keywords.

## 🚀 Features

- ✅ Tamil-style syntax for variables, conditionals, loops, functions, and I/O
- ✅ Clean and readable language for beginners and hobbyists
- ✅ Cross-platform CLI
- ✅ VS Code extension with syntax highlighting and file icon support
- ✅ Arithmetic, boolean logic, and built-in functions like `max`, `min`, `pow`
- ✅ Better error messages for easy debugging

---

## 📦 Installation

### 🔵 Windows (Installer)

1. Download the latest `AahaanInstaller.exe` from [Releases](https://github.com/userdevil/aahaan/releases).
2. Run the installer. This will install `aahaan.exe` and set it in your system path.
3. You can now run Aahaan programs via:

```bash
aahaan path/to/yourfile.ahn
```

### 🐧 Linux/macOS (Manual)

1. Clone the repo:
   ```bash
   git clone https://github.com/userdevil/aahaan
   cd aahaan
   ```
2. Make the CLI globally accessible:
   ```bash
   chmod +x aahaan.py
   ln -s $(pwd)/aahaan.py /usr/local/bin/aahaan
   ```
3. Run:
   ```bash
   aahaan file.ahn
   ```

---

## 🧠 Language Example

```ahn
kaatuda greet() {
  ennaachu "Vanakkam da mapla!"
}

greet()

kelu "Enter a number: "
vechutten n = _

irundhaachu (n % 2 == 0) {
  ennaachu "Even Number"
} illana {
  ennaachu "Odd Number"
}
```

---

## 🖍️ VS Code Extension

1. Download the Aahaan VS Code extension from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=MavinSandeep.aahaan&ssr=false#overview)
2. Features:
   - Syntax highlighting for `.ahn` files
   - File icon support (with custom icon)
   - Compatible with `material-icon-theme`, `vs-seti`, etc.

---

## 📚 Keywords (Tamil Dialogues as Commands)

| Keyword        | Meaning                |
|----------------|------------------------|
| `ennaachu`     | `print`                |
| `vechutten`    | variable assignment    |
| `irundhaachu`  | `if`                   |
| `illana`       | `else`                 |
| `vandhacha`    | `while` loop           |
| `kaatuda`      | function definition    |
| `odi`          | return from function   |
| `kelu`         | input from user        |

---

## 🛠 CLI Options

```bash
aahaan yourfile.ahn        # Run Aahaan file
aahaan --version           # Show CLI version
aahaan --debug yourfile.ahn  # Show tokens and AST
```

---

## 📂 Project Structure

```
.
├── aahaan.py              # CLI entry
├── lexer.py               # Tokenizer
├── aahaan_parser.py       # Parser
├── interpreter.py         # Runtime
├── examples/              # Sample .ahn programs
└── README.md
```

---

## 📌 Contributing

Have a cool dialogue you want to turn into a feature? PRs are welcome! 😉

- Submit issues or feature requests
- Fork and submit a pull request
- Tamil Nadu tech pride 💪

---

## 📃 License

MIT License

---

🎬 **Aahaan** – Programming meets Kollywood!
