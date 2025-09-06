#!/usr/bin/env python

import sys
import re

url_pattern = re.compile(r'href="([^"]*)"')

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    urls = url_pattern.findall(line)
    
    for url in urls:
        if url:
            print('%s\t%s' % (url, 1))