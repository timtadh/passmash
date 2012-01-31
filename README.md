Passmash - The Site Specific Password Munger
============================================

Passmash produces a unique password for each site you use based on

- The url (supplied as a command line argument)
- A password (supplied via an interactive prompt)
- A keyfile (located at ~/.ssh/passmash.key)


Usage
-----

There are two ways to use `passmash`

1. Using the `pm` script.

    The `pm` script takes a URL (or other identifier) and prompts for a
    password. It places the derived (generated) password on the clipboard.

        $ pm yoururlhere.com/login

    1. On Linux it uses the `xclip` program. 
    2. On MacOS X it uses `pbcopy`.
    3. On Windows it uses `clip`.

2. Invoking the python module directly. 

    Alternatively you can invoke the module directly

        $ python -m passmash anyurlhere.com/login
    
    It will pipe the derived (generated) password to stdout (fd 1) and place all
    other output (such as prompts and error information) on stderr (fd 2).
        

Setup
-----

### Install Dependencies


- Linux [Debian Compatible Instructions]
    - Install Python 2.7.x (Tested, 2.6 may work)
      
            $ sudo apt-get install python2.7
         
    - Install `pip`
        
            $ sudo apt-get install python-pip

    - [Optional] Install `xclip` (needed for automatic clipboard copying)
      
            $ sudo apt-get install xclip

- Mac OS X
  
    (If you use a Mac please submit a pull request pointing to resources for this)

    - Install Python 2.7.x (Tested, 2.6 may work)
    - Install `pip`

- Windows

    (If you use Windows please submit a pull request pointing to resources for this)

    - Install Python 2.7.x (Tested, 2.6 may work)
    - Install `pip`
    

### Install Passmash

    $ [sudo] pip install --src="$HOME/.src" -e git://github.com/timtadh/passmash.git#egg=passmash

### Updating
  
    $ [sudo] pip install -U --src="$HOME/.src" -e git://github.com/timtadh/passmash.git#egg=passmash

### Setting up the Key File
    
We recommend the keyfile be random data. The following command generates 512
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
-----------------

    h = hmac.new(key, password, sha256)
    h.update(url)
    for i in xrange(250000):
        h.update(h.digest())
    return h.digest()


