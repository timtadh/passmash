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

