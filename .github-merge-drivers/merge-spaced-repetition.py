#!/usr/bin/env python3

import sys
import re

# Paths to the files involved in the merge
ancestor_file = sys.argv[1]
current_file = sys.argv[2]
  other_file = sys.argv[3]

# Read the contents of the files
with open(ancestor_file, 'r') as f:
    ancestor = f.read()
with open(current_file, 'r') as f:
    current = f.read()
with open(other_file, 'r') as f:
    other = f.read()

# Define a regex pattern to match the spaced repetition comments
sr_pattern = re.compile(r'<!--SR:![^>]+-->')

# Remove SR comments from the ancestor and other versions
ancestor_clean = sr_pattern.sub('', ancestor)
other_clean = sr_pattern.sub('', other)

# If the cleaned versions are the same, prefer the current version (with SR comments)
if ancestor_clean == other_clean:
    with open(current_file, 'w') as f:
        f.write(current)
else:
    # Otherwise, perform a standard merge (you might want to improve this part)
    with open(current_file, 'w') as f:
        f.write(other)

sys.exit(0)