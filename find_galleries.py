#!/usr/bin/env python3
import re
from pathlib import Path

html_file = Path("C:/Users/L33/.openclaw/workspace/projects/aqua-terra/index.html")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

print("Gallery sections found:")
for m in re.finditer(r'id="([^"]*gallery[^"]*)"', content):
    print(f"  - {m.group(1)}")
