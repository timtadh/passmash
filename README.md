Passmash - The Site Specific Password Munger
============================================

Passmash produces a unique password for each site you use based on

- The url (supplied as a commandline argument)
- A password (supplied via an interactive prompt)
- A keyfile (located at ~/.ssh/passmash.key)


Usage
=====

You can use the module directly via 

    $ python -m passmash anyurlhere.com/login | xclip -selection clipboard

Which will place the password in your clipboard without echoing it to the console.

Alternatively, you can use a convience script which does the same thing (should
work for Linux, Mac and Windows).

    $ pm yoururlhere.com/login


Setup
-----

    $ pip install --src="$HOME/.src" -e git://github.com/timtadh/passmash.git#egg=passmash

### Updating
  
    $ pip install -U --src="$HOME/.src" -e git://github.com/timtadh/passmash.git#egg=passmash

### Setting up the Key File
    
We recomend the keyfile be random data. The following command generates 512
bytes of data from the unlimited random byte generator.

    $ head -c 512 /dev/urandom > ~/.ssh/passmash.key

This command does the same thing but from the slightly more secure limited
random byte generator. May be slow.

    $ head -c 512 /dev/random > ~/.ssh/passmash.key

Finally, you can use any key length (I recommend 512 bytes as the minimum). This
command generates 16384 bytes (16 KB) of data from the unlimited generator. 

    $ head -c 16384 /dev/urandom > ~/.ssh/passmash.key


Syntax
------

    usage: passmash [options] url 

    Options
        -h, help                     Display this message
        -c, clamp=N                  Don't output more than N characters
        -v, version                  Version information


Hashing Algorithm
=================

The hashing algorithm is:

    h = hmac.new(key, password, sha256)
    h.update(url)
    for i in xrange(250000):
        h.update(h.digest())
    return h.digest()


