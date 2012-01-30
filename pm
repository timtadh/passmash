#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Tim Henderson
#Email: tim.tadh@hackthology.com
#For licensing see the LICENSE file in the top level directory.

import os, sys, subprocess

# python -m passmash $@ | xclip -selection clipboard

if __name__ != '__main__': raise RuntimeError, "Can only be run as main"

if os.name == 'posix':
    clipper = ['xclip', '-selection', 'clipboard']
elif os.name == 'darwin':
    clipper = ['pbcopy']
elif os.name == 'windows':
    clipper = ['clip']
else:
    raise RuntimeError, "We don't yet support %s" % (os.name,)

args = sys.argv[1:]
pm = subprocess.Popen(['python', '-m', 'passmash'] + args, stdout=subprocess.PIPE)
out, err = pm.communicate()
if pm.returncode == 0:
    clip = subprocess.Popen(clipper, stdin=subprocess.PIPE)
    clip.communicate(out)

