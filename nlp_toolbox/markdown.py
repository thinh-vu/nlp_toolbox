## merge markdown files into a single one
import glob
import fileinput
import os

def markdown_marge(path, lmt='/'):
    pat = os.path.expanduser(f'{path}{lmt}*.md')
    with open('markdown_combined.md', 'w') as f:
        # for line in sorted(fileinput.input(glob.glob(pat))):
        for line in fileinput.input(glob.glob(pat)):
            f.write(line)
    message = 'Please find the combine markdown file at: ' + f'{path}{lmt}markdown_combined.md'
    return message
