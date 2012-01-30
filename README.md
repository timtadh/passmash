Passmash - The Site Specific Password Munger
============================================

Passmash produces a unique password for each site you use based on

- The url (supplied as a commandline argument)
- A password (supplied via an interactive prompt)
- A keyfile (located at ~/.ssh/passmash.key)


Usage
=====

    $ passmash anyurlhere.com/login | xclip -selection clipboard

Will place the password in your clipboard without echoing it to the console.


Syntax
------

    usage: passmash [options] url 

    Options
        -h, help                     Display this message
        -c, clamp=N                  Don't output more than N characters
        -v, version                  Version information


Setting up the Key File
-----------------------
    
We recomend the keyfile be random data. eg.

    $ head -c 512 /dev/urandom > ~/.ssh/passmash.key


Hashing Algorithm
=================

The hashing algorithm is:

    h = hmac.new(key, password, sha256)
    h.update(url)
    for i in xrange(250000):
        h.update(h.digest())
    return h.digest()


