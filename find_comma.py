import re
import sys

def check_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    
    # regex for "word, word and word" or "word, word or word"
    # missing the oxford comma
    # roughly: \b(\w+(?:\s+\w+)*),\s+([\w\s]+)\s+(and|or)\s+(\w+)
    # actually, just look for ", \w+ and " or ", \w+ or " where there is no comma before and
    
    matches = re.finditer(r'([A-Za-z]+(?:\s+[A-Za-z]+)?(?:,\s+[A-Za-z]+(?:\s+[A-Za-z]+)?)+)\s+(and|or)\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)', text)
    for m in matches:
        print(filename, m.group(0))

check_file('index.qmd')
check_file('README.md')
check_file('AGENTS.md')
