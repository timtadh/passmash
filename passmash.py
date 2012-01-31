#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Tim Henderson
#Email: tim.tadh@hackthology.com
#For licensing see the LICENSE file in the top level directory.

import sys, os
from getpass import getpass
from getopt import getopt, GetoptError
import hmac
from hashlib import sha256

RELEASE = 'master'

usage_message = \
'''usage: passmash [options] url '''

extended_message = \
'''
Options
    -h, help                     Display this message
    -c, clamp=N                  Don't output more than N characters
    -v, version                  Version information

Explanation
    Produces a password for a website based on
        - url (supplied as a commandline argument)
        - password (supplied at interactive prompt)
        - keyfile (located at ~/.ssh/passmash.key)
    
    We recomend the keyfile be random data. eg.

        $ head -c 512 /dev/urandom > ~/.ssh/passmash.key

    The hashing algorithm is:

        h = hmac.new(key, password, sha256)
        h.update(url)
        for i in xrange(25000):
            h.update(h.digest())
        return h.digest()
'''

error_codes = {
    'usage':1,
    'version':2,
    'option':3,
}

def keyfile():
    keyfile = os.path.expanduser('~/.ssh/passmash.key')
    with open(keyfile, 'rb') as f:
        key = f.read()
    return key

def mash(key, url, password):
    h = hmac.new(key, password, sha256)
    h.update(url)
    for i in xrange(250000):
        h.update(h.digest())
    return h.digest()

def pretty(hash):
    return hash.encode('base64').strip().rstrip('=')

def log(msg):
    print >>sys.stderr, msg

def output(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()

def usage(code=None):
    '''Prints the usage and exits with an error code specified by code. If code
    is not given it exits with error_codes['usage']'''
    log(usage_message)
    if code is None:
        log(extended_message)
        code = error_codes['usage']
    sys.exit(code)


def main():
    try:
        opts, args = getopt(sys.argv[1:],
            'hvc:',
            ['help', 'version', 'clamp='])
    except GetoptError, err:
        log(err)
        usage(error_codes['option'])
    
    url = ' '.join(args).strip()
    if not url:
        usage()
    
    clamp = None
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--version'):
            log(RELEASE)
            sys.exit(error_codes['version'])
        elif opt in ('-c', '--clamp'):
            clamp = int(arg)
   
    key = keyfile()
    password = getpass()
    mashed = pretty(mash(key, url, password))
    if clamp is None: clamp = len(mashed)
    output(mashed[:min(clamp, len(mashed))])
    log('')


if __name__ == '__main__':
    main()

