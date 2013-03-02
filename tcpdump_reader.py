#!/usr/bin/python

import sys
import re

IP_REGEX = re.compile('[0-9\.]+\s>\s[0-9\.]+')

data = ''

while 1:
    try:
        data += sys.stdin.read(1)
        if data.endswith('\n'):
            ip_string = IP_REGEX.findall(data[:-1])
            print ip_string[0] if ip_string else ''
            sys.stdout.flush()
            data = ''
    except KeyboardInterrupt:
        sys.stdout.flush()
        break
