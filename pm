#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Tim Henderson
#Email: tim.tadh@hackthology.com
#For licensing see the LICENSE file in the top level directory.

import os, sys, subprocess, platform

# python -m passmash $@ | xclip -selection clipboard

if __name__ != '__main__': raise RuntimeError, "Can only be run as main"

system = platform.system().lower()  

clipper = None
if system == 'linux':
    clipper = ['xclip', '-selection', 'clipboard']
elif system == 'darwin':
    clipper = ['pbcopy']
elif system == 'windows':
    clipper = ['clip']
else:
    print >>sys.stderr, "We don't yet support %s for autoclipboard copying" % (platform.system(),)

args = sys.argv[1:]
pm = subprocess.Popen(['python', '-m', 'passmash'] + args, stdout=subprocess.PIPE)
out, err = pm.communicate()
if clipper is not None and pm.returncode == 0:
    clip = subprocess.Popen(clipper, stdin=subprocess.PIPE)
    clip.communicate(out)
else:
    print out
    print ' - '.join(out[i:i+5] for i in xrange(0, len(out), 5))

