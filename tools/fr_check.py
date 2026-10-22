#!/usr/bin/env python3
"""French typography + banned-word check for the Construire Fiable assets.

Usage: python3 fr_check.py [--fix] FILE...
--fix inserts a non-breaking space (U+00A0) before ? : ! ; where a normal
space or no space precedes them in prose (skips URLs, CSS, times like 23h59).
Always reports banned whole words and the pronoun "on".
"""
import re
import sys

BANNED = ["on", "révolutionnaire", "hack", "magique", "facile", "garanti", "secret"]
NBSP = "\u00a0"


def fix_text(text, is_html):
    out = []
    in_style = False
    for line in text.split("\n"):
        if is_html and "<style" in line:
            in_style = True
        if in_style or line.strip().startswith(("http", "<meta", "<link")):
            out.append(line)
            if is_html and "</style>" in line:
                in_style = False
            continue
        # normal space before ? ! ; :  -> nbsp
        line = re.sub(r" ([?!;:])", NBSP + r"\1", line)
        # no space before ? ! (word char or closing guillemet) -> nbsp, but not in URLs
        line = re.sub(r"(?<=[\w»)])([?!])(?=[\s<\"']|$)", NBSP + r"\1", line)
        out.append(line)
    return "\n".join(out)


def strip_markup(text):
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text


def main():
    fix = "--fix" in sys.argv
    files = [a for a in sys.argv[1:] if a != "--fix"]
    total = 0
    for path in files:
        text = open(path, encoding="utf-8").read()
        is_html = path.endswith(".html")
        if fix:
            new = fix_text(text, is_html)
            if new != text:
                open(path, "w", encoding="utf-8").write(new)
                text = new
        prose = strip_markup(text)
        for n, line in enumerate(prose.split("\n"), 1):
            low = line.lower()
            for w in BANNED:
                for m in re.finditer(rf"(?<![\w'’-]){re.escape(w)}(?![\w'’-])", low):
                    total += 1
                    print(f"BANNED  {path}:{n}: «{w}» … {line.strip()[:110]}")
            if re.search(r"\s[?!;:]", line.replace(NBSP, "")) and re.search(r" [?!;:]", line):
                total += 1
                print(f"SPACE   {path}:{n}: espace normale avant ponctuation … {line.strip()[:90]}")
        print(f"checked {path}")
    print(f"{total} problems")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
