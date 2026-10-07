import re

def fix_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Simple regex to find lists without Oxford comma.
    # It looks for word, word(s) and word(s)
    # Be careful not to replace it if it's already there or not a list.
    pass

